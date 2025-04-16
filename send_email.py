import smtplib
from email.message import EmailMessage
import psycopg2


def get_latest_update(user, password, dbname, table, host='localhost', port=5432):
    try:
        with psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM {table} ORDER BY id DESC LIMIT 1;")
                row = cur.fetchone()

                if row:
                    return "\n".join([f"{str(value)}" for i, value in enumerate(row)])
                else:
                    return "No data available."
    except Exception as e:
        return f"Error fetching data: {e}"


def send_email(sender, recipient, password, content, subject="Daily Update"):
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(content)

    try:
        with smtplib.SMTP_SSL("74.125.24.108", 465) as server:
            server.login(sender, password)
            server.send_message(message)
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")


# === Configuration ===
DB_CONFIG = {
    'user': 'postgres',
    'password': 'password',
    'dbname': 'daily_updates',
    'table': 'daily_update',
    'host': 'localhost',
    'port': 5432
}

EMAIL_CONFIG = {
    'sender': 'sender_email',
    'recipient': 'reciever_email',
    'password': 'Gmail App Password'
}


# === Run the script ===
latest_update = get_latest_update(**DB_CONFIG)
email_body = f"Hey!\n\nHere's the latest daily update:\n\n{latest_update}"
send_email(content=email_body, **EMAIL_CONFIG)
