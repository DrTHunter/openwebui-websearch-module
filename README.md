# 📧 OpenWebUI SMTP Email Service

A lightweight, modular microservice that enables Open-WebUI agents and tools to securely send email through any SMTP provider.

Whether you’re building automation agents, notification systems, personal assistants, or workflow AIs, this service gives your local models the ability to send structured, authenticated emails — safely and efficiently.

---

## 📌 Overview

This service provides a clean bridge between **Open-WebUI** and **SMTP email infrastructure**, allowing AI agents to send messages without exposing credentials or requiring complex backend code.

With this tool, your local AI gains:

✉️ Automated email sending
📨 Multi-recipient support
🔐 Secure, environment-based credential loading
⚙️ Modular Tools class for reuse in other utilities
🎛️ Production-ready FastAPI architecture

Drop it directly into Open-WebUI and empower your agents with real email-sending capabilities.

---

## ⚙️ Features

* 🧩 **FastAPI server** designed for local AI agent calls
* 🔐 **Environment-based SMTP authentication**
* 🔁 **Reusable Tools class** for email handling
* 📬 **POST /send_email** endpoint
* ⚡ Lightweight & dependency-minimal
* 🪟 Runs on Windows, Linux, and Docker
* 🔌 Perfect for modular Open-WebUI extensions

---

## 📁 Project Structure

```
openwebui-smtp-email-service/
├── mail_service.py          # FastAPI API service
├── smtp_tools.py            # Email-sending Tools class
├── smtp_email.env           # SMTP credentials (never commit real ones)
├── docker-compose.yml       # One-command Docker launcher
├── run_email_service.bat    # Windows launcher
├── requirements-smtp.txt    # Dependency list
└── README.md
```

---

# 🔧 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/DrTHunter/openwebui-smtp-email-service.git
cd openwebui-smtp-email-service
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements-smtp.txt
```

---

## 3️⃣ Environment Setup

Edit `smtp_email.env`:

```env
FROM_EMAIL="your_email@example.com"
PASSWORD="your_app_specific_password"
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=465
```

> ⚠️ Never commit smtp_email.env with real values to GitHub.

---

# ▶️ Running the Service

## 🪟 Windows

Run:

```
run_email_service.bat
```

Or manually:

```bash
python mail_service.py
```

Service available at:

```
http://127.0.0.1:8000
```

---

# 🐳 Running with Docker (One Command)

With Docker Compose, launching the full service is as simple as:

```bash
docker compose up -d
```

Your `docker-compose.yml`:

```yaml
services:
  smtp-email-service:
    build: .
    container_name: smtp-email-service
    restart: unless-stopped
    ports:
      - "8000:8000"
    env_file:
      - smtp_email.env
```

Service will be live at:

```
http://localhost:8000
```

---

# 📡 Example Request

```bash
curl -X POST "http://127.0.0.1:8000/send_email" \
  -H "Content-Type: application/json" \
  -d "{\"subject\":\"Test Email\", \"body\":\"Hello world!\", \"recipients\":[\"example@example.com\"]}"
```

---

# 🧩 Integration with Open-WebUI

To use this tool **directly inside Open-WebUI**, go to:

### **Workspace → Tools → Add New Tool**

Then paste the full contents of:

```
smtp_tools.py
```

…into the code window, like this:

![OpenWebUI Tools Screenshot](https://github.com/DrTHunter/openwebui-websearch-module/blob/main/assets/open_web_ui_new_tool.png?raw=true)

Once added, your local models can call:

```
http://localhost:8000/send_email
```

Your LLM can now send secure, authenticated emails as part of its workflows — perfect for:

* Workflow automation
* Daily reports
* Personal assistant features
* System alerts
* Notification pipelines

---

# 🎉 You’re Ready to Go

This tool is:

* Easy to run
* Easy to extend
* Easy to integrate
* Designed for Open-WebUI

---

# 📜 License

### Creative Commons Attribution–NonCommercial 4.0 International (CC BY-NC 4.0)

### © 2026 Trent Hunter

This project is licensed under the CC BY-NC 4.0 license.

You are free to:
* Share — copy and redistribute the material
* Adapt — remix, transform, and build upon it

Under the following terms:
* Attribution — You must give appropriate credit.
* Non-Commercial — You may not use the material for commercial purposes.

Full license text:
https://creativecommons.org/licenses/by-nc/4.0/legalcode
