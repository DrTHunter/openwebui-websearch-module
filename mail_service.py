# mail_service.py

"""
Mail Service
A FastAPI microservice for sending emails using SMTP credentials
stored in a local .env file.
"""

import os
import smtplib
from email.mime.text import MIMEText
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator

# Import the Tools class
from webui import Tools

# Path to your .env config file (users should replace this with their own)
CONFIG_PATH = "./email.env"

app = FastAPI(
    title="Email Service",
    description="A simple SMTP email-sending API"
)

# Initialize Tools instance
tools = Tools(config_path=CONFIG_PATH)


# -------------------------
# Request Model
# -------------------------

class EmailRequest(BaseModel):
    subject: str
    body: str
    recipients: List[str]

    @validator("subject")
    def subject_non_empty(cls, v):
        if not v.strip():
            raise ValueError("Subject cannot be empty")
        return v.strip()

    @validator("body")
    def body_non_empty(cls, v):
        if not v.strip():
            raise ValueError("Body cannot be empty")
        return v.strip()

    @validator("recipients")
    def recipients_non_empty(cls, v):
        if not v or len(v) == 0:
            raise ValueError("Recipients list cannot be empty")
        return v


# -------------------------
# Routes
# -------------------------

@app.post("/send_email")
async def send_email(email_request: EmailRequest):
    """
    Sends an email using SMTP configuration from the Tools class.
    """
    try:
        result = tools.send_email(
            subject=email_request.subject,
            body=email_request.body,
            recipients=email_request.recipients
        )

        if "successfully" in result.lower():
            return {
                "status": "ok",
                "message": "Email sent successfully",
                "details": {
                    "subject": email_request.subject,
                    "recipients": email_request.recipients,
                },
            }

        raise HTTPException(status_code=500, detail=f"Failed to send email: {result}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "Email service is running"}


@app.get("/server-status")
async def server_status():
    """
    Shows SMTP status as loaded from the config.
    """
    try:
        has_credentials = bool(tools.valves.FROM_EMAIL and tools.valves.PASSWORD)
        return {
            "server_configured": has_credentials,
            "from_email": tools.valves.FROM_EMAIL if has_credentials else "Not configured",
            "smtp_server": tools.valves.SMTP_SERVER,
            "smtp_port": tools.valves.SMTP_PORT,
        }
    except Exception as e:
        return {"server_configured": False, "error": str(e)}


@app.get("/tools-status")
async def tools_status():
    """Returns basic information about configuration."""
    try:
        return {
            "tools_initialized": True,
            "from_email": tools.valves.FROM_EMAIL,
            "smtp_server": tools.valves.SMTP_SERVER,
            "smtp_port": tools.valves.SMTP_PORT,
            "config_path": CONFIG_PATH,
        }
    except Exception as e:
        return {
            "tools_initialized": False,
            "error": str(e),
        }


# -------------------------
# Local Development Run
# -------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
