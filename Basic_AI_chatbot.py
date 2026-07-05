import requests


API_KEY = 
API_URL = 

system_prompt = {
    "role": "system",
    "content": "You are a helpful and friendly professional assistant."
}

conversation_history = [system_prompt]

print("Chatbot is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": conversation_history
    }

    response = requests.post(API_URL, headers=headers, json=body)
    data = response.json()

    ai_reply = data["choices"][0]["message"]["content"]

    conversation_history.append({
        "role": "assistant",
        "content": ai_reply
    })

    print(f"AI: {ai_reply}\n")