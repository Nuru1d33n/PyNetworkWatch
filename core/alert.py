# core/alert.py
import smtplib
from email.message import EmailMessage
import os

class AlertManager:
    def __init__(self):
        # Retrieve SMTP configuration from environment variables for security
        self.smtp_server = os.getenv("SMTP_SERVER", "sandbox.smtp.mailtrap.io")
        self.port = int(os.getenv("SMTP_PORT", 587))
        self.sender_email = os.getenv("SENDER_EMAIL", "temmylhardey@gmail.com")
        self.receiver_email = os.getenv("RECEIVER_EMAIL", "temmylhardey@gmail.com")
        self.username = os.getenv("SMTP_USERNAME", "7d568db2a22346")
        self.password = os.getenv("SMTP_PASSWORD", "90c452ef4cfdd7")  # Ideally, keep this out of the code directly

    def send_alert(self, ip, mac):
        """Send alert when a new device is detected."""
        print(f"Sending alert: New device detected - IP: {ip}, MAC: {mac}")

        # Compose the email message
        message = f"Alert: Unauthorized device detected! IP: {ip}, MAC: {mac}"
        email_msg = EmailMessage()
        email_msg.set_content(message)
        email_msg['Subject'] = 'Unauthorized Device Alert'
        email_msg['From'] = self.sender_email
        email_msg['To'] = self.receiver_email

        # Send the email
        try:
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Secure the connection
                server.login(self.username, self.password)
                server.send_message(email_msg)
                print("Alert sent successfully.")
        except Exception as e:
            print(f"Error sending email alert: {e}")

# Use environment variables for sensitive data and keep it out of the code:
# Example .env file:
# SMTP_SERVER=sandbox.smtp.mailtrap.io
# SMTP_PORT=587
# SENDER_EMAIL=temmylhardey@gmail.com
# RECEIVER_EMAIL=alert_receiver@example.com
# SMTP_USERNAME=7d568db2a22346
# SMTP_PASSWORD=90c452ef4cfdd7

# Load the environment variables using dotenv (optional)
# If using dotenv, add `from dotenv import load_dotenv` and `load_dotenv()`
