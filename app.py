from flask import Flask, render_template, request# used to create web app
from twilio.rest import Client  # to send whatsapp messages
from datetime import datetime   # to handle date and time
import time                  # to create delay

app = Flask(__name__)# initialize Flask app

account_sid='enter your account_sid here'# Twilio Account SID
auth_token='enter your auth_token here'   # Twilio Auth Token

client=Client(account_sid, auth_token)  # initialize Twilio Client

def send_whatsapp_message(recipient_number, message_body):  # function to send WhatsApp message
    try:    #try to send message
        message=client.messages.create( # send message using Twilio API
            from_='whatsapp:enter your twilio whatsapp number here',  # Twilio WhatsApp number
            body=message_body,               # message content
            to=f'whatsapp:{recipient_number}'   # recipient number
        )   
        print(f'Message sent! SID: {message.sid}')
    except Exception as e:  # handle exceptions
        print(f'Failed: {e}')   

@app.route('/') # route for home page
def index():    #index function to render home page
    return render_template('index.html')    # render index.html template    

@app.route('/send', methods=['POST'])   # route to handle form submission   
def send():  # send function to process form data
    name = request.form['name'] # get recipient name from form
    recipient_number = request.form['number']   #get recipient number from form
    message_body = request.form['message']  # get message body from form
    date_str = request.form['date']  # get scheduled date from form
    time_str = request.form['time'] # get scheduled time from form

    schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")   # parse date and time
    current_datetime = datetime.now()   # get current date and time
    delay_seconds = (schedule_datetime - current_datetime).total_seconds()  # calculate delay in seconds

    if delay_seconds <= 0:  # check if scheduled time is in the past
        return "❌ Time is in the past" # return error message

    time.sleep(delay_seconds)   # wait until scheduled time
    send_whatsapp_message(recipient_number, message_body)   # send WhatsApp message

    return f"✅ Successfully! Message Sented To {name}" # return success message

if __name__ == '__main__':  #used to run the app
    app.run(debug=True) # run Flask app in debug mode
