  # NetSage_AI

NetSage-AI is a Python-based network troubleshooting and diagnosis project designed to assist students and beginners in understanding common networking problems through structured analysis. The project focuses on a practical set of network troubleshooting scenarios rather than trying to act as a large-scale enterprise network management system.

The current version of NetSage-AI works with 30 network troubleshooting cases. Each case contains relevant Cisco CLI output representing a particular networking problem. These cases cover common issues that can occur while configuring and maintaining computer networks, including duplicate IP addresses, incorrect subnet masks, gateway mismatches, interfaces being down, missing VLAN configurations, missing routes, and other configuration-related problems.

The project follows a structured troubleshooting workflow in which the provided network information and CLI output are analyzed to identify the possible fault. The system uses predefined rules, structured data, and AI-assisted diagnosis to generate a meaningful explanation of the detected problem. The objective is not only to identify an error but also to provide information that can help a user understand why the problem occurred and what areas of the network configuration should be checked.

NetSage-AI also includes a collection of test cases and validation scripts to verify different parts of the troubleshooting workflow. The project contains separate components for data handling, rule-based checking, AI-assisted diagnosis, validation, testing, and an interactive dashboard. This modular structure makes it easier to understand how the different stages of the system work together.

The dashboard provides a simple visual representation of the available troubleshooting information and project results. Supporting datasets are stored in structured formats such as CSV and JSON, while documentation and prompt files are maintained separately to make the project easier to study, modify, and extend.

The main purpose of NetSage-AI is educational and experimental. It demonstrates how traditional rule-based network troubleshooting can be combined with AI-assisted reasoning to create a more understandable diagnostic workflow. The project can be useful for students studying Computer Networks, Cisco networking, network troubleshooting, Python programming, and introductory applications of AI in technical problem solving.

NetSage-AI is intentionally kept relatively small and focused. It is not intended to replace professional network monitoring or enterprise network management tools. Instead, it provides a controlled environment containing representative networking problems that can be used to understand troubleshooting concepts, experiment with diagnostic logic, and explore how AI can assist in explaining technical network issues.

The project can also be extended in the future by adding more network fault scenarios, expanding the dataset, introducing additional Cisco CLI commands, improving the diagnostic rules, adding more validation tests, and enhancing the dashboard with additional visualizations and troubleshooting information.
