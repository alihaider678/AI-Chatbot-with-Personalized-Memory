import requests
import json
from config import GEMINI_API_KEY

GEMINI_MODEL_NAME = "gemini-1.5-flash"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1/models/{GEMINI_MODEL_NAME}:generateContent"

def get_gemini_response(user_input: str, memory: str = None):
    headers = {"Content-Type": "application/json"}

    if memory and "on" in memory:
        memory_text = f"You previously mentioned: {memory}"
    else:
        memory_text = memory if memory else "No relevant memory found."

    history_prompt = f"""
    You are an AI assistant that recalls past interactions when relevant.
    - Only mention past memories if they are directly relevant.
    - Avoid inserting timestamps unless the user asks 'when' or 'last time'.

    Past Memory: "{memory_text}"

    User: {user_input}
    AI:
    """

    payload = {
        "contents": [{"parts": [{"text": history_prompt}]}],
        "generationConfig": {"temperature": 0.7, "maxOutputTokens": 200}
    }

    response = requests.post(
        f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except KeyError:
            return "Error: Response format unexpected."
    else:
        return f"Error: {response.status_code} - {response.text}"


if __name__ == "__main__":
    test_cases = [
        ("When did I last drink water?", "You mentioned drinking water 5 minutes ago."),
        ("What was the last thing I said?", "You last mentioned drinking water."),
        ("Tell me something about my day.", "You haven't shared much today. Would you like to talk about something specific?")
    ]

    for user_input, memory in test_cases:
        response = get_gemini_response(user_input, memory)
        print(f"User: {user_input}")
        print(f"Gemini AI Response: {response}\n")
