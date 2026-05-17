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
            input = "Make a fake email that replicates the 'security error' emails that Google or Microsoft likes to send to users, like 'Your account has been compromised' or 'Security Threat' or 'New login detected, please verify' but you don't have to use the examples. Use 'example@example.com' for the email and also don't make any JavaScript or any code or any links. Mailto links are forbidden. Only write the email and don't say anything else."
        )

        if "example@example.com" in response.output_text:

            email_list = ["alert@m1crosoft.com", "no-reply@mIcrosoft.com", "alert@m1crosoft.ca", "no-reply@mIcroSoft.ca","no-reply@google.ca", "no-reply@gogle.com", "alert@googe.com", "alert@google.ca"]

            email_num = randint(0,8)

            email_address = str(email_list[email_num])
            
            response.output_text = response.output_text.replace("example@example.com", email_address)

        if response.output_text != None:
            return response.output_text

    except Exception as exception:
        return f"Exception: {str(exception)}"
