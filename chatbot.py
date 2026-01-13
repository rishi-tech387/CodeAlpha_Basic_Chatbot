# Task 4: Basic Rule-Based Chatbot
# CodeAlpha Internship

def chatbot():
    print("Chatbot: Hello! Type 'hello', 'how are you', or 'bye' to chat.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


# Run the chatbot
chatbot()

