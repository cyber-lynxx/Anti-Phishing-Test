import os
from openai import OpenAI
from flask import Flask
api_key = os.getenv("API_KEY")

app = Flask(__name__)

#Get the different excerpts that we need.
def extract(text, start, end):
    excerpt_start = text.find(start)
    excerpt_end = text.find(end)
    return text[excerpt_start+len(start):excerpt_end].strip()

# Store the excerpts in these variables to make sure they are global
excerpt1 = ""
excerpt2 = ""
excerpt3 = ""
excerpt4 = ""
excerpt5 = ""

#Getting the output from the AI
def generate_email():
    global excerpt1, excerpt2, excerpt3, excerpt4
    
    client = OpenAI(api_key)

    response = client.responses.create(
    model = "gpt-5-mini",    
    prompt = "This is a program to teach the user to determine what a phishing email is. The user will choose whether they think it is a phishing email or not. Your job is to generate these emails, and choose whether or not you want to generate a phishing email. Write 'start of email' when you begin to write the email, and write 'end of email' when you are done. Don't forget to generate a subject. Say 'start of subject' when before write the subject and write 'end of subject' at the end. Keep the exact formatting and capitalization of the keywords as given above. You will also provide the answer to whether or not it is a phishing email. Provide a detailed explanation in bullet point form, but you can use dashes instead of bullet points. Write 'start of answer and explanation' when you start writing what the answer is and why. Write 'end of answer and explanation' when you are done. Then, write 'here is the answer' and, in all caps, tell the answer, which is 'YES' or 'NO'. Then say, 'answer finished'. Don't forget to give the sender (whether or not they are a normal person or a threat actor) an email address and a name. Common fake email addresses include but are not limited to: m1crosoft.com, gmaiI.com, etc. Write 'address start' before you write the address, and 'address end' when you finish. Keep the exact formatting and capitalization of the keywords as given above. When you generate the email address, please do not include any links to mail to that address (including but not limited to: mailto links). You are forbidden to add any JavaScript code, nor any other type of code."
    )

    text = response.output_text

    excerpt1 = extract(text, "start of email", "end of email")
    excerpt2 = extract(text, "start of answer and explanation", "end of answer and explanation")
    excerpt3 = extract(text, "here is the answer", "answer finished")
    excerpt4 = extract(text, "start of subject", "end of subject")
    excerpt5 = extract(text, "address start", "address end")
    
generate_email()

#Sending the strings/excerpts over to a JavaScript File for it to get printed on the HTML
@app.route("/excerpt1")
def send_string1():
    return excerpt1

@app.route("/excerpt2")
def send_string2():
    return excerpt2

@app.route("/excerpt3")
def send_string3():
    return excerpt3

@app.route("/excerpt4")
def send_string4():
    return excerpt4
  
@app.route("/excerpt5")
def send_string5():
    return excerpt5
