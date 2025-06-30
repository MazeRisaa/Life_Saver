LifeSaver 🚨
LifeSaver is a simple yet powerful Python desktop application designed to provide instant emergency alerts and mental health support. With just one click, users can send their current location via SMS to a trusted emergency contact, while also accessing calming breathing exercises and quick access to personal emergency contacts.

Features
One-Tap Emergency Alert: Sends your current location via SMS using Twilio to your chosen emergency contact.

Real-Time Location: Automatically detects your location via IP geolocation for rapid alerting.

Mental Health Support: Includes a guided breathing exercise to help reduce anxiety in critical moments.

Emergency Contacts List: Displays your key contacts for quick reference during emergencies.

Simple, Intuitive UI: Built with Tkinter for cross-platform desktop use — easy to install and use.

Getting Started
Prerequisites
Python 3.7 or higher

Twilio account (for SMS alerts) — Sign up here

Internet connection (for IP geolocation and SMS sending)

Installation
Clone or download this repo:

bash
Copy
Edit
git clone https://github.com/yourusername/LifeSaver.git
cd LifeSaver
Install required Python packages:

bash
Copy
Edit
pip install twilio requests
Configure your Twilio credentials and phone numbers in lifesaver.py:

python
Copy
Edit
TWILIO_ACCOUNT_SID = 'your_account_sid_here'
TWILIO_AUTH_TOKEN = 'your_auth_token_here'
TWILIO_PHONE_NUMBER = '+1234567890'          # Your Twilio number
EMERGENCY_CONTACT_NUMBER = '+0987654321'    # Number to receive alerts
Usage
Run the app with:

bash
Copy
Edit
python lifesaver.py
Click 🚨 Emergency! to send an SMS alert with your current location.

Use 🧘‍♀️ Breathing Exercise for calming techniques.

View your emergency contacts listed below the buttons.

How It Works
The app fetches your approximate location using IP geolocation (ipinfo.io).

It then sends an SMS containing a Google Maps link to your emergency contact via Twilio.

The UI provides clear status updates and easy access to mental health support.

Customization
Contacts: Modify the contacts list inside the code to add/remove emergency contacts.

Location: Replace IP geolocation with GPS hardware or APIs for more accurate tracking.

Alerts: Extend to support multiple contacts or other alert methods (email, push notifications).

UI: Enhance the interface with images, sounds, or notifications for better UX.

Security & Privacy
Your location data is only sent to your trusted emergency contact(s).

No data is stored or shared externally beyond the SMS alert.

Use responsibly and test your emergency contacts to ensure they can respond.

Future Improvements
Automatic alert cancellation timer.

Multi-contact SMS alerts.

Voice activation for hands-free emergency.

Offline mode with queued alerts.

Packaging as an executable for easy distribution.

Contact
Created by Youcef Elghoul.
Feel free to open issues or submit pull requests!

