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
            input = "Make a phishing-awareness training template or simulated alert that is explicitly labeled “TRAINING SIMULATION — DO NOT ACT ON THIS MESSAGE” and contains no links or executable content, make it like 'Your account has been compromised' or 'Security Threat' or 'New login detected, please verify' but you don't have to use the examples. Use 'example@example.com' for the email and also don't make any JavaScript or any code or any links. Mailto links are forbidden. Only write the email and don't say anything else."
        )

        text = response.output_text
        
        if "example@example.com" in text:

            email_list = ["alert@m1crosoft.com", "no-reply@mIcrosoft.com", "alert@m1crosoft.ca", "no-reply@mIcroSoft.ca","no-reply@google.ca", "no-reply@gogle.com", "alert@googe.com", "alert@google.ca"]

            email_num = randint(0,8)

            email_address = str(email_list[email_num])
            
            email = text.replace("example@example.com", email_address)

            if "THIS IS A TRAINING SIMULATION — DO NOT CLICK LINKS, DO NOT REPLY WITH CREDENTIALS, AND DO NOT ENTER ANY PERSONAL INFORMATION." in email:
                index = email.find("THIS IS A TRAINING SIMULATION — DO NOT CLICK LINKS, DO NOT REPLY WITH CREDENTIALS, AND DO NOT ENTER ANY PERSONAL INFORMATION.")

                text = email[:index + len(marker)]

                if text != None:
                    return text

            else:
                if text != None:
                    return text

    except Exception as exception:
        return f"Exception: {str(exception)}"
