import tkinter as tk
from tkinter import messagebox
import threading
import requests
from twilio.rest import Client

# === Twilio config - replace with your real credentials and numbers ===
TWILIO_ACCOUNT_SID = 'your_account_sid_here'
TWILIO_AUTH_TOKEN = 'your_auth_token_here'
TWILIO_PHONE_NUMBER = '+1234567890'
EMERGENCY_CONTACT_NUMBER = '+0987654321'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def get_real_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        loc = data.get('loc')
        if loc:
            lat_str, lng_str = loc.split(',')
            return float(lat_str), float(lng_str)
    except Exception as e:
        print(f"Error getting real location: {e}")
    # fallback coords (Budapest)
    return 47.4979, 19.0402

def send_sms_alert(lat, lng):
    message_body = f"🚨 Emergency Alert! Location: https://maps.google.com/?q={lat},{lng}"
    message = client.messages.create(
        body=message_body,
        from_=TWILIO_PHONE_NUMBER,
        to=EMERGENCY_CONTACT_NUMBER
    )
    return message.sid

def on_emergency_click():
    btn.config(state=tk.DISABLED)
    status_var.set("Getting your location...")

    def task():
        try:
            lat, lng = get_real_location()
            status_var.set(f"Location found: {lat}, {lng}")
            status_var.set("Sending SMS alert...")
            sid = send_sms_alert(lat, lng)
            status_var.set(f"Alert sent! SID: {sid}")
        except Exception as e:
            status_var.set(f"Error sending alert: {e}")
        finally:
            btn.config(state=tk.NORMAL)

    threading.Thread(target=task).start()

def show_breathing_exercise():
    messagebox.showinfo("Breathing Exercise",
        "Try this simple exercise:\n\n"
        "1. Breathe in slowly through your nose for 4 seconds.\n"
        "2. Hold your breath for 7 seconds.\n"
        "3. Exhale slowly through your mouth for 8 seconds.\n\n"
        "Repeat 3 times to help reduce anxiety.")

root = tk.Tk()
root.title("LifeSaver - Emergency Alert")

status_var = tk.StringVar(value="")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="LifeSaver 🚨\nSimple Emergency Alert\n", font=("Arial", 16))
label.pack()

btn = tk.Button(frame, text="🚨 Emergency!", font=("Arial", 18), fg="white", bg="#d93025", command=on_emergency_click)
btn.pack(pady=10)

status_label = tk.Label(frame, textvariable=status_var, font=("Arial", 12))
status_label.pack(pady=(0, 20))

mental_btn = tk.Button(frame, text="🧘‍♀️ Breathing Exercise", font=("Arial", 14), command=show_breathing_exercise)
mental_btn.pack()

# Emergency contacts display
contacts = [
    {"name": "Mom", "phone": "+1234567890"},
    {"name": "Dad", "phone": "+0987654321"},
    {"name": "Best Friend", "phone": "+1122334455"},
]

contacts_frame = tk.Frame(frame)
contacts_frame.pack(pady=10)

tk.Label(contacts_frame, text="Emergency Contacts:", font=("Arial", 14, "underline")).pack()

for c in contacts:
    tk.Label(contacts_frame, text=f"{c['name']}: {c['phone']}", font=("Arial", 12)).pack()

root.mainloop()
