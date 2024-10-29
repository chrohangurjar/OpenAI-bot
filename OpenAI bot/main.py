import openai

# Replace with your OpenAI API key
openai.api_key = 'xxxxxxxx'


def chat_with_gpt(prompt):
    # Use the new completion interface
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if available
        prompt=prompt,
        max_tokens=100,  # Limit the number of tokens in the response
        temperature=0.7  # Control the randomness of responses
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    print("Chatbot: Hello! Ask me anything. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        bot_response = chat_with_gpt(user_input)
        print(f"Chatbot: {bot_response}")
