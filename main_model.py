import os

from mistralai import Mistral, UserMessage
api_key = "gjcMXdlvyyuPtC4caJ5OqGjPYsmMVGxz"
## finetuning

model = "mistral-large-latest"
client = Mistral(api_key= api_key)

messages = []

def ask_chatbot(question):
    messages.append({"role": "user", "content": question})

    response = client.chat.complete(
        model=model,
        messages=messages,
    )

    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})

    return answer

# Example usage:
while True:
    question = input("You: ")
    if question.lower() in ["quit", "exit"]:
        break
    answer = ask_chatbot(question)
    print(f"Bot: {answer}\n")