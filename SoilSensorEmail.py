# Program Title: Soil Moisture Sensor with Email Notifications
# Program Description: This script uses a soil moisture sensor connected to Raspberry Pi.
# It takes 4 readings at 3-hour intervals and sends a numbered email after each reading
# to notify whether the plant needs watering.
# Name: Liu Zibo
# Student ID: 20110005@mail.wit.ie(SETU)/202283890001(NUIST)
# Course & Year: Project Semester 3 & Third-year
# Date: 2025-04-21

import smtplib
from email.message import EmailMessage
from gpiozero import Button
import time

# ========== Email Configuration ==========
from_email_addr = "2145035449@qq.com"         # Sender email address
from_email_pass = "airhzqxcdasadgda"          # QQ Email Authorization Code
to_email_addr = "785214433@qq.com"            # Recipient email address

# ========== GPIO Sensor Setup ==========
channel = 21  # GPIO pin connected to the soil sensor
sensor = Button(channel)

# ========== Moisture Check & Email Function ==========
def check_moisture_and_send_email(reading_number):
    if sensor.is_pressed:
        status = "Water NOT needed"
        body = f"# {reading_number}: Soil is moist. No need to water the plant."
    else:
        status = "Please water your plant"
        body = f"# {reading_number}: Soil is dry. Please water your plant."

    print(f"Status: {status}")  # Print moisture status to terminal

    # ====== Compose and Send Email ======
    msg = EmailMessage()
    msg.set_content(body)
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = f"Plant Status Update #{reading_number}: {status}"

    try:
        server = smtplib.SMTP('smtp.qq.com', 587)
        server.starttls()
        server.login(from_email_addr, from_email_pass)
        server.send_message(msg)
        print(f"Email #{reading_number} sent")
    except Exception as e:
        print(f"Failed to send email #{reading_number}: {e}")
    finally:
        server.quit()

# ========== Main Program ==========
print("Starting SoilSensorEmail script...")
for i in range(4):
    reading_number = i + 1
    print(f"\n--- Reading #{reading_number} ---")
    check_moisture_and_send_email(reading_number)
    if i < 3:
        print("Waiting 3 hours before next reading...")
        time.sleep(10800)  # Wait 3 hours (10800 seconds) between readings

print("\nAll 4 readings completed. Script finished.")
