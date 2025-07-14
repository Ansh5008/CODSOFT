import re
import datetime

# Function to greet the user
def greet_user():
    print("ChatBot: Hello! I'm your friendly chatbot. How can I help you today?")

# Function to get current time
def get_current_time():
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}."

# Function to match user input and respond accordingly
def get_bot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if re.search(r'\b(hi|hello|hey|good morning|good evening)\b', user_input):
        return "Hello! How can I assist you?"

    # Asking for bot's name
    elif re.search(r'\b(your name|who are you)\b', user_input):
        return "I'm ChatBot, your virtual assistant."

    # Asking about the weather (dummy response)
    elif re.search(r'\b(weather|temperature|rain)\b', user_input):
        return "I'm not connected to the internet, but I hope the weather is great where you are!"

    # Asking for time
    elif re.search(r'\b(time|clock|current time)\b', user_input):
        return get_current_time()

    # Asking about creator
    elif re.search(r'\b(who created you|your creator|made you)\b', user_input):
        return "I was created by a Python developer using simple rules."

    # Thank you
    elif re.search(r'\b(thank you|thanks)\b', user_input):
        return "You're welcome!"

    # Exit
    elif re.search(r'\b(bye|exit|quit|goodbye)\b', user_input):
        return "Goodbye! Have a great day!"

    # Default response
    else:
        return "I'm sorry, I don't understand that. Can you rephrase?"

# Main function to run the chatbot
def run_chatbot():
    greet_user()
    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print("ChatBot:", response)

        if re.search(r'\b(bye|exit|quit|goodbye)\b', user_input.lower()):
            break

# Run the chatbot
if __name__ == "__main__":
    run_chatbot()
