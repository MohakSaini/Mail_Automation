import smtplib
from email.message import EmailMessage

def send_email(subject, body, to_email):
    EMAIL_ADDRESS = "YOUR_EMAIL"
    EMAIL_PASSWORD = "APP_PASSWORD"  # App password, not your login password

    # Create the email message
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    # Send the email
    try:
        with smtplib.SMTP_SSL("74.125.24.108", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")

# Test the function
send_email(
    "Hello from Python",
    "This is a test email sent from Python!",
    "RECIEVERS_EMAIL"
)
