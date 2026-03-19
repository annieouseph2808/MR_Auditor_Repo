# 🤖 AI PR Auditor

**AI PR Auditor** is a high-performance GitHub Action that acts as an automated Senior Product Engineer. It reviews every Pull Request in seconds, identifying security vulnerabilities, logic bugs, and code smells before they ever hit your production branch.

---

## 🚀 Features

* **Security First:** Automatically detects hardcoded secrets, API keys, and common vulnerabilities like SQL Injection.
* **Logic Analysis:** Identifies potential edge cases and "off-by-one" errors in your code changes.
* **Lightning Fast:** Powered by Groq (Llama-3) for near-instant feedback.
* **Clean Integration:** Provides feedback directly as a comment on your Pull Request.

---

## 🛠️ Quick Start

To add the AI Auditor to your repository, create a file at:

```
.github/workflows/ai-review.yml
```

and paste the following:

```yaml
name: AI Code Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Run AI Auditor
        uses: annieouseph2808/MR_Auditor_Repo@v1.0.4
        with:
          groq_api_key: ${{ secrets.GROQ_API_KEY }}
```

---

## ⚙️ Configuration

### **Required Secrets**

* **GROQ_API_KEY:** Obtain a free API key from the Groq Console https://console.groq.com/keys . Add it to your repository under
  `Settings > Secrets and variables > Actions`.

### **Permissions**

Ensure your GitHub Action has Read and Write permissions to post comments:

* Go to `Settings > Actions > General`
* Under **Workflow permissions**, select **Read and write permissions**

---

## 🏗️ Technical Architecture

This project is built using a modern DevOps stack to ensure portability and speed:

* **Python 3.11:** Core logic for diff extraction and API orchestration
* **Docker:** The Action is containerized to ensure a consistent environment across any GitHub runner
* **PyGitHub:** For seamless interaction with the GitHub REST API
* **Groq Cloud API:** Utilizing Llama-3 models for high-reasoning code analysis

---

## 🤝 Contributing

This is an open-source project. If you find a bug or have a feature request, please open an issue or submit a Pull Request!

---

## 👨‍💻 Developed by

**Annie Ouseph**

---
