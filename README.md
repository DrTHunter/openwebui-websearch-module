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

Drop it into your Open-WebUI tools directory and power up your agent workflows instantly.

---

## ⚙️ Features

* 🧩 **FastAPI server** designed for local AI agent calls
* 🔐 **Environment-based SMTP authentication**
* 🔁 **Reusable Tools class** for email handling
* 📬 **POST /send_email** endpoint
* ⚡ Lightweight & dependency-minimal
* 🪟 Fully compatible with Windows, Linux, and Docker
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
git clone [https://github.com/<your-username>/openwebui-smtp-email-service](https://github.com/DrTHunter/openwebui-websearch-module).git
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

## 🪟 Windows (Recommended)

Run:

```
run_email_service.bat
```

Or manually:

```bash
python mail_service.py
```

The service will be available at:

```
http://127.0.0.1:8000
```

---

# 🐳 Running with Docker (One Command)

With Docker Compose, launching the full service is as simple as:

```bash
docker compose up -d
```

Your `docker-compose.yml` should look like:

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

This gives users:

* 🟢 One-command startup
* 🟢 Automatic restart
* 🟢 Environment-file injection
* 🟢 Clean log management
* 🟢 Easy updates (`docker compose pull` if you publish an image later)

Service will be live at:

```
http://localhost:8000
```

---

# 📡 Example Request

Send an email with curl:

```bash
curl -X POST "http://127.0.0.1:8000/send_email" \
  -H "Content-Type: application/json" \
  -d "{\"subject\":\"Test Email\", \"body\":\"Hello world!\", \"recipients\":[\"example@example.com\"]}"
```

---

# 🧩 Integration with Open-WebUI

Point your agent/tool configuration at:

```
http://localhost:8000/send_email
```

Your LLM can now send secure, authenticated emails as part of its workflows — perfect for:

* Workflow automation
* Daily reports
* Personal assistant features
* System alerts
* Scheduled summaries
* Notification pipelines

---

# 🎉 You’re Ready to Go

This tool is:

* Easy to run
* Easy to extend
* Easy to integrate
* Perfect for Open-WebUI agents


Just tell me the next step.
