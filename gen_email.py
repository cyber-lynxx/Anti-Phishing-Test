import os
from random import randint
from openai import OpenAI
from flask import Flask

API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

text = "none"

#Getting the output from the AI
def generate_email():
    try:
        global text
        
        client = OpenAI(api_key = API_KEY)
    
        response = client.responses.create(
            model = "gpt-5-mini",    
            input = "Make a phishing-awareness training template or simulated alert. Include a disclaimer before the email starts that says: “TRAINING SIMULATION — DO NOT ACT ON THIS MESSAGE”. The email must not contain any links or executable content. Choose a number between 1 and 10. If it is greater than 5, then make a simulated alert/phishing-awareness training template. Otherwise, make a duplicate of a legit secrutiy alert that appications give when something happens. Make it similar to this example: 'TRAINING SIMULATION — DO NOT ACT ON THIS MESSAGE *newline* From: example@example[.]com *newline* To: [Your Email Address] *newline* Subject: Security Alert — Unusual Sign‑in Detected *newline* Hello, We detected a sign‑in attempt for your account from a new device and location. *newline* Account: [Your Email Address] *newline* Activity detected: Unusual sign‑in from an unrecognized device *newline* Device type: [Device name] *newline* Location: Washington, USA *newline* If this activity was not performed by you, your account may be at risk and will be temporarily restricted until verification is completed. Please verify your account immediately to prevent suspension. If this were a real incident, contact your IT or security team using your organization’s official support channels (do not use any contact details that may appear in suspicious messages). *newline* Sincerely, Security Operations Team' For the Location, you may choose any city in the world. For device type, you can choose any device that exists to replace the '[Device name]', and an exampls is Windows. Do not give the user any hints as to whether or not it is a duplicate of a legit one or if it is a training template simulating a phishing email, as this is a test. At the very very end, say this exact sentence with the exact same punctuation and spelling: 'My number was' and then say your number."
        )

        text = response.output_text
        
        if "example@example[.]com" in text:

            email_list = ["alert@m1crosoft.com", "no-reply@mIcrosoft.com", "alert@m1crosoft.ca", "no-reply@mIcroSoft.ca","no-reply@google.ca", "no-reply@gogle.com", "alert@googe.com", "alert@google.ca"]

            email_num = randint(0,7)

            email_address = str(email_list[email_num])
            
            email = text.replace("example@example[.]com", email_address)

        if email != None:
            return email

        else:
            email = "Value is None"
            return email

    except Exception as exception:
        return f"Exception: {str(exception)}"

generate_email()

#Sending the output to the JavaScript file to be put onto the HTML page
@app.route("/text")
def send_string1():
    return generate_email()
