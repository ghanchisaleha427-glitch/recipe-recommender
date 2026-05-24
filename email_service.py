import smtplib
import random
from email.mime.text import MIMEText

SENDER_EMAIL = "smartrecipea@gmail.com"
APP_PASSWORD = "yoef ohbw kvit opup"   # तुम्हारा Gmail App Password

def send_otp(receiver_email):
    otp = str(random.randint(100000, 999999))
    msg = MIMEText(f"Your OTP is {otp}")
    msg["Subject"] = "Signup OTP"
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER_EMAIL, APP_PASSWORD)
    server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
    server.quit()
    return otp
