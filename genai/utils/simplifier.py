import google.generativeai as genai

# 🔐 Setup Gemini
genai.configure(api_key="AIzaSyCcICS7GqRCmsloDAaWnD9oGF6CSiWPobc")
model = genai.GenerativeModel("gemini-pro")

def get_summary(text):
    prompt = f"Summarize this into 4 short bullet points:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text

def simplify_text(text):
    prompt = f"Explain this to a 10-year-old using very simple English:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text
