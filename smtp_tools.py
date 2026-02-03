# smtp_tools.py

"""
SMTP Email Tools
Utility class for sending emails using SMTP credentials
stored inside a .env file.

This file is fully sanitized and safe to publish publicly.
"""

import smtplib
from email.mime.text import MIMEText
from typing import List, Optional

from pydantic import BaseModel, Field


class ToolsValves(BaseModel):
    FROM_EMAIL: str = Field(
        default="",
        description="The email address used for sending messages",
    )
    PASSWORD: str = Field(
        default="",
        description="SMTP/App password for the sender email",
    )
    SMTP_SERVER: str = Field(
        default="smtp.gmail.com",
        description="SMTP server address",
    )
    SMTP_PORT: int = Field(
        default=465,
        description="SMTP server port number",
    )


class Tools:
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize Tools instance and optionally load SMTP settings
        from a .env configuration file.
        """
        if config_path:
            self.valves = self._load_config_from_file(config_path)
            print(f"Configuration loaded from {config_path}")
            print(f"SMTP Server: {self.valves.SMTP_SERVER}:{self.valves.SMTP_PORT}")
            print(f"From Email: {self.valves.FROM_EMAIL}")
            print(f"Password: {'*' * len(self.valves.PASSWORD)}")
        else:
            self.valves = ToolsValves()
            print("Warning: No config path provided. Email sending will not work.")

    def _load_config_from_file(self, config_path: str) -> ToolsValves:
        """
        Load SMTP configuration from a .env file.

        Expected format:
            KEY=value

        Returns:
            ToolsValves with populated fields
        """
        config_dict = {}

        try:
            with open(config_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue

                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip()

                    # Remove surrounding quotes
                    if (value.startswith("'") and value.endswith("'")) or (
                        value.startswith('"') and value.endswith('"')
                    ):
                        value = value[1:-1]

                    config_dict[key] = value

            # Check required fields
            for field in ["FROM_EMAIL", "PASSWORD"]:
                if field not in config_dict or not config_dict[field]:
                    raise ValueError(f"Missing required field in config: {field}")

            return ToolsValves(
                FROM_EMAIL=config_dict["FROM_EMAIL"],
                PASSWORD=config_dict["PASSWORD"],
                SMTP_SERVER=config_dict.get("SMTP_SERVER", "smtp.gmail.com"),
                SMTP_PORT=int(config_dict.get("SMTP_PORT", 465)),
            )

        except Exception as e:
            print(f"Error loading config from {config_path}: {e}")
            raise

    def send_email(self, subject: str, body: str, recipients: List[str]) -> str:
        """
        Send an email.

        Args:
            subject: Email subject
            body: Email body text
            recipients: List of recipient email addresses

        Returns:
            Status string describing the result
        """
        try:
            if not self.valves.FROM_EMAIL or not self.valves.PASSWORD:
                error_msg = (
                    "Error: SMTP credentials not configured
