import random
import re
from datetime import datetime
from intents import intents


class RuleBasedChatbot:
    def __init__(self):
        self.intents = intents

    def clean_text(self, text):
        text = text.lower().strip()
        text = re.sub(r"[^\w\s]", "", text)
        return text

    def get_response(self, message):
        message = self.clean_text(message)

        # Date
        if "date" in message:
            return f"📅 Today's date is {datetime.now().strftime('%d %B %Y')}."

        # Time
        if "time" in message:
            return f"🕒 Current time is {datetime.now().strftime('%I:%M %p')}."

        # Match predefined intents
        for intent in self.intents:
            for pattern in intent["patterns"]:
                if pattern in message:
                    return random.choice(intent["responses"])

        # Default response
        return random.choice(self.intents[-1]["responses"])