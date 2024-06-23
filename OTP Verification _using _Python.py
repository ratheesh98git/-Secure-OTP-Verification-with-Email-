import os
import math
import random
import smtplib

def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def send_otp_email(receiver_email, otp):
    sender_email = "your@gmail.com"
    password = "your_app_password"

    subject = "OTP Verification"
    body = f"Your OTP is: {otp}"

    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print("OTP sent successfully to your email.")
    except Exception as e:
        print(f"Error: {e}")
        print("Failed to send OTP. Please check your internet connection and try again.")

def verify_otp(expected_otp):
    user_input = input("Enter Your OTP: ").strip()
    if user_input == expected_otp:
        print("OTP Verified")
    else:
        print("OTP Verification Failed. Please check your OTP again.")

def main():
    otp = generate_otp()
    print(f"Generated OTP: {otp}")

    email_id = input("Enter your email address: ").strip()
    send_otp_email(email_id, otp)

    verify_otp(otp)

if __name__ == "__main__":
    main()
