# tests/test_gemini.py

import os
import google.generativeai as genai

def test_gemini_connection():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ GOOGLE_API_KEY not found in environment variables.")
        return

    genai.configure(api_key=api_key)

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content("Hello Gemini, this is a connection test!")
        print("✅ Gemini connection successful!")
        print("Response:", response.text)

    except Exception as e:
        print("❌ Gemini test failed:", str(e))


if __name__ == "__main__":
    print("Running Gemini API test...\n")
    test_gemini_connection()
