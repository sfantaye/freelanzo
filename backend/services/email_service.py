import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

NYLAS_API_URL = os.getenv("NYLAS_API_URL")
NYLAS_ACCESS_TOKEN = os.getenv("NYLAS_ACCESS_TOKEN")

# Send an email reminder for unpaid invoices
def send_invoice_reminder(client_email: str, invoice_number: str, due_date: str):
    email_body = f"""
    Dear Client,

    This is a reminder that your invoice #{invoice_number} is due on {due_date}. Kindly make the payment to avoid any penalties.

    Best regards,
    Freelanzo Team
    """

    email_data = {
        "to": [{"email": client_email}],
        "subject": f"Invoice #{invoice_number} Reminder",
        "body": email_body
    }

    headers = {
        "Authorization": f"Bearer {NYLAS_ACCESS_TOKEN}",
    }

    response = requests.post(f"{NYLAS_API_URL}/send", json=email_data, headers=headers)
    return response.json()
