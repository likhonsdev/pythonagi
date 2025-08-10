import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def generate_response(prompt):
  """Generates a response from the Gemini model."""
  model = genai.GenerativeModel('gemini-1.5-flash')
  chat = model.start_chat()
  return chat