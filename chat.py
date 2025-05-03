def chatbot_response(user_input):
    user_input = user_input.lower()

    # Keyword-based responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing fine! How about you?"
    elif "your name" in user_input:
        return "I'm a customer service chatbot."
    elif "help" in user_input:
        return "Sure! I can help you with product inquiries, order status, and general questions."
    elif "order" in user_input:
        return "Are you asking about your order status or placing a new order?"
    elif "product" in user_input:
        return "We offer a variety of products. Could you specify what you’re looking for?"
    elif "price" in user_input:
        return "Prices vary depending on the product. Do you have something specific in mind?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    
    # Fallback response
    return "I'm sorry, I didn't catch that. Could you rephrase your question?"

def main():
    print("Customer Support Chatbot")
    print("Type 'bye' to exit")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()


 