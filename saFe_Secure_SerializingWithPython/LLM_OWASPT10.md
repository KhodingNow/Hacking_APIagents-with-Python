Prompt Injection - crafted inputs leading to data leaks, misinformation, unauthorized actions. Mitigations = privilege controls and human oversight for critical systems.
Insecure Output handling - Accepting LLM outputs without validation exposes backend systems to attacks like - XSS, CSRF, or RCE. Mitigate by ZERO trust systems, input sanitization
Training Data Poisoning - tampering with training data introduces bias / vulnerabilities . Mitigate by vetting data sources by Machine Learning Bill of Materials (ML-BOM).
Model Denial of Service (Unbounded Consumption) - Resource heavy inputs can degrade performance or inflate costs. MITIGATE by input validation, rate limit.
Supply chain vulnerabilities - third party datasets, pre trained models. Mitigate by Auditing suppliers and monitor components.
Sensitive Information Disclosure - LLMs can leak information via outputs. Mitigate by scrubbing Training Data
Insecure Pluging Design - Weak access or pluggins enable RCE - Enforce parameterized inputs and minimal permissions
Excessive Agency - Overprivileged LLMs can autonomously perform harmful actions (send unauthorized emails). Mitigate by restricting permissions, and implement guardrails.
Overreliance - Blind trust on LLMs risk misinformation. Mitigate by checking with external sources.
Model Theft - Unauthorized copying of propietary models harms competitiveness. Audit model repos, strong access controls