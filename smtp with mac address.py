import smtplib
import uuid
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to get MAC address
def get_mac_address():
    mac = ':'.join(format((uuid.getnode() >> elements) & 0xFF, '02x') for elements in range(0, 6*8, 8))
    return mac

# Function to get current date and time
def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Email credentials
sender_email = "s2110476128@ru.ac.bd"
sender_password = ""  # Use environment variables for security
receiver_email = "conovix984@bitflirt.com"

# Create email message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Test Email with MAC Address & Timestamp"

# Get MAC address and timestamp
mac_address = get_mac_address()
current_time = get_current_time()

# Email body
body = f"""Hello, this is a test email sent from Python.

MAC Address: {mac_address}
Timestamp: {current_time}
"""
msg.attach(MIMEText(body, "plain"))

# Sending email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
