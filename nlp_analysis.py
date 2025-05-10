# nlp_analysis.py
from openai import OpenAI

client = OpenAI(api_key="your_api_key")

def analyze_challenge(challenge):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a startup mentor."},
            {"role": "user", "content": f"My challenge: {challenge}. What stage does this belong to?"}
        ]
    )
    return response.choices[0].message.content

