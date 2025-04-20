import os
from dotenv import load_dotenv
from google import genai

load_dotenv()  # Load environment variables from .env file

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

client = genai.Client(api_key=api_key)

def run():
  response = client.models.generate_content(
      model="gemini-2.0-flash",
      contents=["How does AI work?"]
  )
  print(response.text)

run()