import openai
from config import Config

def summarize_text(text):
    """Summarizes a long transcript using OpenAI's GPT-4 API."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert summarizer. Provide a concise summary of the given transcript."},
                {"role": "user", "content": text}
            ],
            max_tokens=200
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print("Error:", e)
        return "Failed to generate summary."
