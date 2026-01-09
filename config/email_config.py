from email.mime import message
from http import server
import smtplib
from email.mime.text import MIMEText

def send_email(receiver, subject, body):
    print("Starting email script...")

    sender = "tanishagupta231@gmail.com"
    receiver = receiver
    password = "yrym ydng oplq muua"

    print("Creating email content...")

    # Create the email content
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver
    print("Connecting to Gmail SMTP server...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    print("Starting TLS encryption...")
    server.starttls()  # encrypt connection

    print("Logging in...")
    server.login(sender, password)
    print("Sending email...")
    server.sendmail(sender, receiver, message.as_string())  # IMPORTANT

    print("Email sent successfully!")

    print("Closing server connection...")
    server.quit()

    print("Program finished.")
