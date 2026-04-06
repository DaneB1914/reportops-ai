# ReportOps AI 🔐

An AI-powered penetration testing report generator that converts structured vulnerability data into professional, client-ready reports.

## 🚀 Features

* Generate detailed vulnerability reports using AI
* CLI-based workflow for automation
* JSON-driven input for scalability
* Multi-vulnerability processing
* Structured output (Markdown)
* Custom severity scoring logic

## 📦 Tech Stack

* Python
* LLM Integration (Groq / Gemini)
* JSON-based data pipeline

## 🛠️ Usage

```bash
python main.py --input findings.json --output output/report.md
```

## 📄 Example Input

```json
[
  {
    "title": "Cross-Site Scripting (XSS)",
    "endpoint": "/search",
    "method": "GET",
    "attack_vector": "network",
    "complexity": "low",
    "privileges_required": "none",
    "description": "Reflected XSS in search parameter"
  }
]
```

## 📊 Output

* Executive Summary
* Findings Breakdown
* AI-generated remediation steps
* Severity classification

## ⚠️ Disclaimer

This tool is intended for educational and professional penetration testing use only.

## 📌 Roadmap

* CVSS scoring implementation
* PDF export
* Web interface
* Automated scanning integration

---

Built by Dane Babcock
