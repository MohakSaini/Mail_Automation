import smtplib

try:
    with smtplib.SMTP("smtp.dotsquare.com", 465) as server:
        server.starttls()
        server.ehlo()
        print("Connected successfully")
except Exception as e:
    print("SMTP connection failed:", e)
