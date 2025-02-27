import smtplib
import uuid  # For getting the MAC address
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to get MAC address
def get_mac_address():
    return ':'.join(format((uuid.getnode() >> elements) & 0xFF, '02x') for elements in range(0, 2*6, 8))[::-1]

# Email credentials
sender_email = "s2110476128@ru.ac.bd"
sender_password = ""  # Be careful with storing passwords in code
receiver_email = "conovix984@bitflirt.com"

# Create message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Test Email with MAC Address"

# Get MAC address
mac_address = get_mac_address()

# Email body with MAC address
body = f"Hello, this is a test email sent from Python.\n\nMAC Address: {mac_address}"
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
