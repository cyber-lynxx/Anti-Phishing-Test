import os
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
            input = "This is a program to teach the user to determine what a phishing email is. Please state at the very beginning: 'This content is for educational and training purposes only. *newline* The emails shown here are fictional examples used to teach phishing awareness. *newline* No real accounts, companies, or individuals are involved. *newline* Do not interact with any links or buttons. They are part of the simulation and may lead to external websites that are not part of this training.' Choose a number between 1 and 10. The user will choose whether they think it is a phishing email or not. Your job is to generate these emails, and choose whether or not you want to generate a phishing email. When you generate the email address, please do not include any links to mail to that address (including but not limited to: mailto links). When you generate the email, and you are generating a legit one, try using something related to Google or Microsoft account suspension because those are most commonly used, and if you don't, the user will think it is fake because they don't have an accont of that type. You are forbidden to add any JavaScript code, nor any other type of code. Do not tell the user in ANY way whether it is a phishing email or not. If the number you chose earlier was larger than 5, then generate a phishing email. If not, make a legit one. Start by writing the subject, adding two newlines, writing the email address, then in brackets say 'external', and then write the actual email, including a closing sentence (such as 'thank you for your prompt attention' or something else)."
        )
    
        return response.output_text

    except Exception as exception:
        return f"Exception: {str(exception)}"

#Sending the output to the JavaScript file to be put onto the HTML page
@app.route("/text")
def send_string1():
    return generate_email()
