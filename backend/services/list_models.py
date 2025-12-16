from google.genai import Client
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the client with your API key
client = Client(api_key=os.getenv("GEMINI_API_KEY"))

# List available models
try:
    models = client.list_models()  # Adjust this method based on the library's documentation
    for model in models:
        print(model.name)
except AttributeError:
    print("The method to list models might be different. Please check the library's documentation.")