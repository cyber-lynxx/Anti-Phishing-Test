import os
from openai import OpenAI
api_key = os.getenv("API_KEY")

#Getting the output from the AI
def generate_email(prompt):
    client = OpenAI(api_key)

    response = client.responses.create(
    model = "gpt-5-mini",    
    input = "This is a program to teach the user to determine what a phishing email is. The user will choose whether they think it is a phishing email or not. Your job is to generate these emails, and choose whether or not you want to generate a phishing email. Write 'start of email' when you begin to write the email, and write 'end of email' when you are done. Keep the exact formatting and capitalization of the keywords as given above. You will also provide the answer to whether or not it is a phishing email. Provide a detailed explanation in bullet point form, but you can use dashes instead of bullet points. Write 'start of answer and explanation' when you start writing what the answer is and why. Write 'end of answer and explanation' when you are done. Then, write 'here is the answer' and, in all caps, tell the answer, which is 'YES' or 'NO'. Then say, 'answer finished'.  Keep the exact formatting and capitalization of the keywords as given above."
    )

    text = tesponse.output_text

    start1 = text.find("start of email")
    end1 = text.find("end of email")
  
    excerpt1 = text[start1+len("start of email"):end1].strip()

  #
    start2 = text.find("start of answer and explanation")
    end2 = text.find("end of answer and explanation")
  
    excerpt2 = text[start2+len("start of answer and explanation"):end1].strip()

    #
    start3 = text.find("here is the answer")
    end3 = text.find("answer finished")
  
    excerpt3 = text[start3+len("here is the answer"):end3].strip()
        
  
