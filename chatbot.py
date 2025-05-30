import random
#! Dictionary of responses based on sentiment

responses = {
    'positive': [
        "That's great to hear!😊",
        "I'm glad, you're feeling good!👍",
        "Keep up the positive vibes!👌",
        "Awesome! Your positivity is contagious😘!"
    ],
    'negative': [
        "I'm sorry to hear that.😔",
        "It's okay to feel down sometimes.",
        "If you need to talk, I'm here for you.🫠",
        "Hang in there, things will get better."
    ],
    'neutral': [
        "I see. How can I assist you further?",
        "Okay, let me know if you need anything.",
        "Got it. If you have any questions, feel free to ask.",
        "Understood. I'm here if you need me."
    ]
}

def get_bot_response(sentiment):
    """
    Return a random response based on the detected sentiment.
    """
    return random.choice(responses.get(sentiment, ["I'm not sure how to respond to that."]))
    return "I'm not sure how to respond to that."