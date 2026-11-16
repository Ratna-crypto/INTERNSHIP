import random
import re
from datetime import datetime

# Define intents with patterns and responses
intents = {
    "greeting": {
        "patterns": [r"\bhello\b", r"\bhi\b", r"\bhey\b", r"\bgood (morning|afternoon|evening)\b"],
        "responses": ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    },
    "goodbye": {
        "patterns": [r"\bbye\b", r"\bgoodbye\b", r"\bsee you\b", r"\bsee you later\b"],
        "responses": ["Goodbye!", "See you later!", "Bye! Come back soon."]
    },
    "thanks": {
        "patterns": [r"\bthanks\b", r"\bthank you\b", r"\bthx\b"],
        "responses": ["You're welcome!", "No problem!", "My pleasure!"]
    },
    "name": {
        "patterns": [r"\bwhat is your name\b", r"\bwho are you\b", r"\byour name\b"],
        "responses": ["I'm a simple chatbot!", "You can call me ChatBot."]
    },
    "time": {
        "patterns": [r"\btime\b", r"\bwhat time is it\b", r"\bcurrent time\b"],
        "responses": []  # handled separately
    }
}

# Function to get chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    for intent, intent_data in intents.items():
        for pattern in intent_data["patterns"]:
            if re.search(pattern, user_input):
                if intent == "time":
                    now = datetime.now().strftime("%H:%M:%S")
                    return f"The current time is {now}"
                return random.choice(intent_data["responses"])

    return "I'm not sure I understood that. Try saying 'hello', asking for the time, or saying 'bye'."

# Main chat loop
if __name__ == "__main__":
    print("ChatBot: Hello! Type 'quit' to exit.")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                print("ChatBot: Goodbye!")
                break
            response = chatbot_response(user_input)
            print("ChatBot:", response)
        except Exception as e:
            print("ChatBot: Oops! Something went wrong:", str(e))
