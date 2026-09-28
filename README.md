# NetSage AI

NetSage AI is a Cisco network troubleshooting assistant that helps engineers diagnose networking issues. It combines deterministic Python rules with Gemini-based reasoning to analyze command-line evidence and suggest accurate fixes.

## Project Overview

NetSage AI is designed to accelerate problem resolution in Cisco environments. By running raw `show` command outputs through a strict deterministic rule checker first, and then passing those findings to the Gemini large language model, the system provides accurate, contextual troubleshooting advice while mitigating the risk of AI hallucination.

The project follows a structured troubleshooting workflow in which deterministic checks provide a reliable foundation before AI-based reasoning is applied. This combination allows the system to analyze network evidence, identify potential issues, generate a diagnosis, and provide a recommended resolution that can then be reviewed and verified by an engineer.

## Why Two Pipelines?

The project includes two distinct execution pipelines to serve different evaluation and operational needs.

### 1. Historical 30-Case Pipeline

The historical pipeline evaluates a fixed set of 30 Cisco troubleshooting cases that are used as a baseline for evaluating the system.

The workflow:

- Evaluates 30 fixed Cisco troubleshooting cases used as a baseline.
- Takes pre-defined evidence from a CSV file.
- Runs deterministic rule checking to identify relevant physical and configuration network states.
- Generates a Gemini diagnosis based on the detected rules and symptoms.
- Validates the generated output against a predefined schema.
- Forces retries when the generated response does not satisfy the required format.
- Includes a Human Review phase to evaluate the accuracy of the AI diagnosis.
- Populates dashboard and evaluation metrics to demonstrate baseline performance.

### 2. Live Interactive Pipeline

The Live Interactive pipeline allows an engineer to investigate a completely new network problem that is not necessarily part of the historical 30-case dataset.

The workflow:

- Allows an engineer to enter a new network troubleshooting problem through the Live Diagnosis interface.
- Takes custom symptoms, topology information, and Cisco `show` command evidence.
- The browser sends the request to `local_server.py`.
- The existing `rule_checker.py` and `diagnose.py` logic are reused for the new input.
- Gemini generates a custom diagnosis based on the available evidence.
- Validation and retry logic ensures that the generated response follows the required JSON structure.
- Human Review allows the engineer to accept, edit, or reject the AI-generated diagnosis.
- Cisco Packet Tracer can be used to manually verify the recommended fix.
- The completed interaction is saved to the Live Session History.

The Live Workflow is an extension of the original 30-case project. It does not replace the historical benchmark or modify the original evaluation dataset.

## Architecture / Data Flow

### Historical Pipeline

```text
30 Cases
    ↓
Evidence
    ↓
Rule Checker
    ↓
Gemini Diagnosis
    ↓
Validation
    ↓
Human Review
    ↓
Dashboard Metrics
