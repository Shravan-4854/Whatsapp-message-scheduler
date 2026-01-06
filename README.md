# WhatsApp Message Scheduler & Auto Sender

A Flask-based web application that allows users to schedule WhatsApp messages and automatically send them at a specified date and time using the Twilio WhatsApp API.

## 🚀 Features
- Schedule WhatsApp messages using date and time
- Automated message delivery via Twilio API
- Form-based input for recipient details
- Validation to prevent scheduling messages in the past
- Responsive and user-friendly UI

## 🛠️ Technologies Used
- Python
- Flask
- Twilio WhatsApp API
- HTML
- CSS

## 📌 How It Works
1. User enters recipient details, message, date, and time.
2. Application calculates delay using Python datetime.
3. Message is sent automatically at the scheduled time via Twilio.

## ⚙️ Setup Instructions
1. Clone the repository
2. Install required dependencies
3. Configure Twilio Account SID and Auth Token
4. Activate WhatsApp Sandbox in Twilio
5. Run the Flask application

## 📷 Note
Twilio WhatsApp Sandbox must be active before sending messages.

## 👨‍💻 Author
Shravan
