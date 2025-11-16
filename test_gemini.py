
import google.generativeai as genai

genai.configure(api_key="AIzaSyAIzKYcpxgdF_Lq88nfUfF5Q7S0mu95ThM")

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Hello Gemini!")
print(response.text)
