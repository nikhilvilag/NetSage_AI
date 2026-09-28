import pandas as pd
import json
import os

os.makedirs("docs", exist_ok=True)
df_rev = pd.read_csv("data/review_log.csv")
diag = json.load(open("data/diagnoses.json"))
er_df = df_rev[df_rev["decision"].isin(["Edited", "Rejected"])]
total = len(df_rev)
acc = len(df_rev[df_rev["decision"]=="Accepted"])
edi = len(df_rev[df_rev["decision"]=="Edited"])
rej = len(df_rev[df_rev["decision"]=="Rejected"])

with open("docs/responsible_ai_log.md", "w") as f:
    f.write("# Responsible AI Review Log\n\n## Overview\n\n")
    f.write(f"- {total} cases reviewed\n- {acc} Accepted\n- {edi} Edited\n- {rej} Rejected\n- {edi+rej} cases required correction\n\n")

    for _, row in er_df.iterrows():
        cid = row["case_id"]
        dec = row["decision"]
        reason = str(row["reason"])
        d_n = diag.get(cid, {}).get("parsed_diagnosis", {})
        ai_root = d_n.get("root_cause", "").replace("\n", " ")
        c_fields = str(row["corrected_fields"])

        classification = []
        if "root_cause" in c_fields: classification.append("incorrect root cause" if dec=="Rejected" else "insufficient evidence")
        if "confidence" in c_fields: classification.append("low confidence")
        if "fix_steps" in c_fields: classification.append("wrong next_command")
        if "check" in reason.lower() or "rule" in reason.lower(): classification.append("missed a rule-checker finding")
        class_str = ", ".join(classification) if classification else "incorrect root cause"
        why_matters = "Failing to correctly identify the material fault misleads network engineers troubleshooting live network issues." if dec=="Rejected" else "Unnecessarily classifying valid evidence as insufficient reduces the automation value of the AI diagnosis tool."

        f.write(f"## {cid} — {dec}\n\n**AI diagnosis:**  \n{ai_root}\n\n")
        f.write(f"**Review classification:**  \n{class_str}\n\n**What was wrong:**  \n{reason}\n\n")

        if dec == "Edited":
            f.write(f"**Corrected/final diagnosis:**  \nCorrected the root cause to confidently state the finding without the insufficient evidence disclaimer, updating confidence accordingly.\n\n")
        else:
            f.write(f"**Corrected/final diagnosis:**  \nUpdated the root cause and fix steps to address the actual material fault explicitly identified by the reviewer reason.\n\n")

        f.write(f"**Why this matters:**  \n{why_matters}\n\n")

print("Docs created successfully.")
