from flask import Flask 
from flask import render_template
from flask import request, redirect

from twilio.rest import TwilioRestClient 

app = Flask(__name__) # Creating the Flask app
client = TwilioRestClient ('TWILIO_ACCOUNT_SID = os.environ['AC12f7fd079b844f469fda25935d665d76']', 'TWILIO_AUTH_TOKEN = os.environ['f6e0055df7c9b31ece2731397dc51773']') # Paste in your AccountSID and AuthToken here
twilio_number = "+1234567890" # Replace with your Twilio number

@app.route("/") # When you go to top page of app, this is what it will execute
def main():
    return render_template('form.html')
  
@app.route("/submit-form/", methods = ['POST']) 
def submit_number():
    number = request.form['number']
    formatted_number = "+1" + number # Switch to your country code of choice
    client.messages.create(to=formatted_number, from_ = twilio_number, body = "Goodwater Test.") # Replace body with your message of choice
    return redirect('/messages/')
  
@app.route("/messages/")
def list_messages():
    messages = client.messages.list(to=twilio_number)
    return render_template('messages.html', messages = messages)
    
    
if __name__ == '__main__': # If we're executing this app from the command line
    app.run("0.0.0.0", port = 3000, debug = True)
