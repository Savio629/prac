from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['how are you?', ['I am good, thank you!', 'I am doing well, thanks for asking!']],
    ['what is your name?', ['My name is Chatbot.', 'I am Chatbot, nice to meet you!']],
    ['quit', ['Bye!', 'Goodbye!', 'Take care!']],
    ['(.*)', ["I'm sorry, I didn't understand that.", 'Could you please rephrase that?']]
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

# Define a function to interact with the chatbot
def chatbot_interaction():
    print("Welcome! Ask me anything or type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() == 'quit':
            break

# Call the function to start interacting with the chatbot
chatbot_interaction()
