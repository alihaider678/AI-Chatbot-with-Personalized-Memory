from chatbot.memory import store_conversation, retrieve_memory
from chatbot.gemini_ai import get_gemini_response

def chatbot(user_input: str):
    memory = retrieve_memory(user_input)

    if memory and memory.lower() in user_input.lower():
        memory = None  

    response = get_gemini_response(user_input, memory)
    store_conversation(user_input)
    return response

if __name__ == "__main__":
    print("🤖 AI Chatbot Started! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        print(f"Bot: {chatbot(user_input)}")
