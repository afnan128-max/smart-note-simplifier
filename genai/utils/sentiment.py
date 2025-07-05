import google.generativeai as genai

genai.configure(api_key="your-gemini-api-key")
model = genai.GenerativeModel("gemini-pro")

def classify_sentiment(text):
    prompt = f"""
Analyze the sentiment of the following input and classify it strictly as 'Positive', 'Neutral', or 'Negative'. 

Text: "{text}"
Respond with just one word: Positive, Neutral, or Negative.
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
