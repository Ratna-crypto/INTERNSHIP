import datetime

def chatbot():
    print("Chatbot: Hi, I’m your chatbot. How can I help you today?")

    while True:
        user_input = input("You: ").lower().strip()

        # Exit condition
        if "bye" in user_input:
            print("Chatbot: Bye! Come back soon.")
            break

        # Greetings
        elif "hi" in user_input or "hello" in user_input:
            print("Chatbot: Hi there!")

        # Feelings
        elif "how are you" in user_input:
            print("Chatbot: I’m a bot so I don’t have feelings, but thanks for asking!")

        # Weather
        elif "weather" in user_input:
            print("Chatbot: Weather seems fine from my side, but you might want to check a weather website for updates.")

        # Time
        elif "time" in user_input:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {now}")

        # Date
        elif "date" in user_input or "today" in user_input:
            today = datetime.date.today().strftime("%B %d, %Y")
            print(f"Chatbot: Today’s date is {today}")

        # Python love
        elif "python" in user_input:
            print("Chatbot: I love Python for its simplicity and power!")

        # Thanks
        elif "thank" in user_input:
            print("Chatbot: My pleasure!")

        # Fallback
        else:
            print("Chatbot: I’m not sure I understood that. Try saying 'hello', asking for the time, date, weather, or saying 'bye'.")

# Run chatbot
chatbot()