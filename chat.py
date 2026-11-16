import random
import re
from datetime import datetime

# Define intents with patterns and responses
intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
        "responses": ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "see you later"],
        "responses": ["Goodbye!", "See you later!", "Bye! Come back soon."]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "thx"],
        "responses": ["You're welcome!", "No problem!", "My pleasure!"]
    },
    "name": {
        "patterns": ["what is your name", "who are you", "your name"],
        "responses": ["I'm a simple chatbot!", "You can call me ChatBot."]
    },
    "time": {
        "patterns": ["time", "what time is it", "current time"],
        "responses": []  # handled separately
    }
}

# Function to get chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    for intent, intent_data in intents.items():
        for pattern in intent_data["patterns"]:
            if re.search(pattern, user_input):
                if intent == "time":
                    now = datetime.now().strftime("%H:%M:%S")
                    return f"The current time is {now}"
                return random.choice(intent_data["responses"])
    
    return "Sorry, I didn't understand that."

# Main chat loop
if __name__ == "__main__":
    print("ChatBot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("ChatBot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("ChatBot:", response)