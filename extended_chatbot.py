import random
import time

# Define various categories of responses
responses = {
    "greeting": [
        "Hi there! How can I assist you today?",
        "Hello! It's great to meet you!",
        "Hey! What's on your mind?",
        "Greetings, my friend! How can I help you?"
    ],
    "how_are_you": [
        "I'm doing well, thank you for asking! How about you?",
        "I'm great, just here to help you out!",
        "I'm doing fantastic! How are you feeling today?",
        "I'm good, thanks for asking! What's going on with you?"
    ],
    "goodbye": [
        "Goodbye! It was great talking to you!",
        "See you later! Have a wonderful day!",
        "Take care! Come back anytime!",
        "Bye for now! Don’t hesitate to reach out if you need anything!"
    ],
    "thanks": [
        "You're welcome! Anytime!",
        "Happy to help! Let me know if you need anything else.",
        "No problem at all!",
        "You're very welcome!"
    ],
    "default": [
        "Sorry, I don't quite understand that.",
        "Could you please rephrase?",
        "I'm not sure how to respond to that.",
        "Hmm... I'm still learning. Can you ask me something else?"
    ],
    "weather": [
        "The weather is looking great today! What’s it like where you are?",
        "I think it's sunny outside! How about where you are?",
        "I bet the weather is perfect for a walk! Do you like going outside?",
        "I don't know the current weather, but it's always sunny in here! 🌞"
    ],
    "hobbies": [
        "What are your hobbies? I enjoy learning about new things!",
        "Do you have any favorite activities? I think hobbies are great for the soul!",
        "What do you like to do in your free time? I'm curious!",
        "I love hearing about hobbies! What's your favorite pastime?"
    ],
    "life_advice": [
        "Remember, every challenge is an opportunity to grow!",
        "Don't be afraid to take risks and learn from them.",
        "Embrace every new day as a chance to make progress.",
        "Take time for yourself and don’t be too hard on yourself."
    ],
    "affirmations": [
        "You're doing great! Keep it up!",
        "You have the strength to overcome anything that comes your way!",
        "Believe in yourself. You're amazing!",
        "You're making progress, and that’s what matters!"
    ],
    "jokes": [
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "Why did the computer go to the doctor? It had a virus!",
        "What do you call fake spaghetti? An impasta!",
        "I told my computer I needed a break, now it won’t stop sending me Kit-Kats!"
    ],
    "random": [
        "Did you know honey never spoils? Archaeologists have found pots of honey in ancient tombs that are still edible!",
        "Bananas are berries, but strawberries are not! Strange, right?",
        "The longest hiccuping spree lasted 68 years! Imagine that.",
        "Octopuses have three hearts, and they can change color depending on their mood."
    ]
}

# Function to generate a response based on user input
def generate_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easier comparison
    
    # Check for greeting-related words
    if any(greeting in user_input for greeting in ["hi", "hello", "hey", "greetings", "morning", "afternoon", "evening"]):
        return random.choice(responses["greeting"])
    
    # Check for how are you queries
    elif any(question in user_input for question in ["how are you", "how's it going", "how do you do"]):
        return random.choice(responses["how_are_you"])
    
    # Check for thanks-related responses
    elif any(phrase in user_input for phrase in ["thank you", "thanks", "thanks a lot", "thank you very much"]):
        return random.choice(responses["thanks"])
    
    # Check for goodbye-related phrases
    elif any(phrase in user_input for phrase in ["bye", "goodbye", "see you", "take care"]):
        return random.choice(responses["goodbye"])
    
    # Check for weather-related queries
    elif "weather" in user_input:
        return random.choice(responses["weather"])
    
    # Check for hobbies-related queries
    elif any(phrase in user_input for phrase in ["hobbies", "favorite activities", "what do you do for fun"]):
        return random.choice(responses["hobbies"])
    
    # Check for life advice
    elif any(phrase in user_input for phrase in ["advice", "life advice", "give me advice"]):
        return random.choice(responses["life_advice"])
    
    # Check for affirmations
    elif any(phrase in user_input for phrase in ["affirmations", "words of encouragement", "positive words"]):
        return random.choice(responses["affirmations"])
    
    # Check for jokes
    elif any(phrase in user_input for phrase in ["tell me a joke", "joke", "make me laugh"]):
        return random.choice(responses["jokes"])
    
    # Check for random trivia
    elif any(phrase in user_input for phrase in ["tell me something random", "random facts", "give me trivia"]):
        return random.choice(responses["random"])
    
    # Default response for unrecognized inputs
    else:
        return random.choice(responses["default"])

# Function to simulate conversation
def chatbot():
    print("Chatbot: Hello! I'm your friendly assistant. Type 'bye' to end the conversation.")
    time.sleep(1)  # Adds a pause for a more conversational flow
    
    while True:
        user_input = input("You: ")  # User input
        
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Get and print the chatbot's response
        response = generate_response(user_input)
        print(f"Chatbot: {response}")
        time.sleep(1)  # Simulate thinking time for a more natural conversation flow

# Start the chatbot
chatbot()
