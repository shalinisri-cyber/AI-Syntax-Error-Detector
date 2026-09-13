import os
from dotenv import load_dotenv
from google import genai

# Load the API key from the .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Check whether the API key is available
if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in the .env file.")

# Create the Gemini client
client = genai.Client(api_key=api_key)


def ask_gemini(code, errors):
    error_text = "\n".join(
        [
            f"Line {error['line']}: {error['type']} - {error['message']}"
            for error in errors
        ]
    )

    prompt = (
        "You are an expert C programming tutor.\n\n"
        "Analyze the following C code and explain its syntax errors "
        "in simple language.\n\n"
        "C code:\n"
        + code
        + "\n\nDetected errors:\n"
        + error_text
        + "\n\nPlease provide:\n"
        "1. Error explanation\n"
        "2. Why the error occurred\n"
        "3. Corrected C code\n"
        "4. Prevention tip\n\n"
        "Do not invent errors that are not present in the code."
    )

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text