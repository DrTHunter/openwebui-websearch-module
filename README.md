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
├── run_email_service.bat    # Windows launcher
├── requirements-smtp.txt    # Dependency list
└── README.md
```

---

# 🔧 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/openwebui-smtp-email-service.git
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

> ⚠️ **Never commit smtp_email.env with real values to GitHub.**

---

# ▶️ Running the Service

## 🪟 Windows (Recommended)

Run:

```
run_email_service.bat
```

Or start manually:

```bash
python mail_service.py
```

The service will be available at:

```
http://127.0.0.1:8000
```

---

# 🐳 Running with Docker

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements-smtp.txt .
RUN pip install -r requirements-smtp.txt

COPY . .

EXPOSE 8000
CMD ["python", "mail_service.py"]
```

---

### Build the image

```bash
docker build -t smtp-email-service .
```

### Run the container

```bash
docker run -d -p 8000:8000 --env-file smtp_email.env smtp-email-service
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

You can plug your agent or automation tool into:

```
http://localhost:8000/send_email
```

Your LLM can now send secure emails natively — perfect for:

* Workflow automations
* Daily summaries
* Alerts & notifications
* Custom assistant agents

---

# 🎉 You're Ready to Go

This tool is easy to run, easy to extend, and fits perfectly into any Open-WebUI workflow.
If you'd like, I can also generate:

✨ `tool.json` (for direct Open-WebUI integration)
✨ A styled logo/banner for the GitHub repo
✨ A setup guide for Linux or macOS
✨ A test client script (Python or JS)

Just tell me, and I’ll build it.
