import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.1-flash-lite")

def generate_response(prompt):

    response = model.generate_content(prompt)

    return response.text