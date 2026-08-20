import re
import random
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# DOWNLOAD REQUIRED NLTK RESOURCES
# ============================================================

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)


class FAQChatbot:

    # ========================================================
    # INITIALIZE CHATBOT
    # ========================================================

    def __init__(self, intents):

        # ----------------------------------------------------
        # Initialize NLP tools
        # ----------------------------------------------------

        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words("english"))

        # ----------------------------------------------------
        # Store intents
        # ----------------------------------------------------

        self.intents = intents

        # ----------------------------------------------------
        # Create lists for patterns, responses and tags
        # ----------------------------------------------------

        self.patterns = []
        self.responses = []
        self.tags = []

        # ----------------------------------------------------
        # Extract information from intents.py
        # ----------------------------------------------------

        for intent in intents:

            tag = intent["tag"]
            intent_responses = intent["responses"]

            for pattern in intent["patterns"]:

                self.patterns.append(pattern)
                self.responses.append(intent_responses)
                self.tags.append(tag)

        # ----------------------------------------------------
        # Preprocess all patterns
        # ----------------------------------------------------

        self.cleaned_patterns = [
            self.preprocess(pattern)
            for pattern in self.patterns
        ]

        # ----------------------------------------------------
        # TF-IDF Vectorizer
        # ----------------------------------------------------

        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            sublinear_tf=True
        )

        # Convert patterns into TF-IDF vectors
        self.tfidf_matrix = self.vectorizer.fit_transform(
            self.cleaned_patterns
        )

        # ----------------------------------------------------
        # Similarity threshold
        # ----------------------------------------------------

        self.threshold = 0.25

    # ========================================================
    # TEXT PREPROCESSING
    # ========================================================

    def preprocess(self, text):

        # ----------------------------------------------------
        # 1. Convert text to lowercase
        # ----------------------------------------------------

        text = text.lower()

        # ----------------------------------------------------
        # 2. Remove punctuation
        # ----------------------------------------------------

        text = re.sub(r"[^\w\s]", "", text)

        # ----------------------------------------------------
        # 3. Tokenize text
        # ----------------------------------------------------

        tokens = word_tokenize(text)

        # ----------------------------------------------------
        # 4. Remove stopwords
        # 5. Apply lemmatization
        # ----------------------------------------------------

        cleaned_tokens = [
            self.lemmatizer.lemmatize(word)
            for word in tokens
            if word not in self.stop_words
        ]

        # ----------------------------------------------------
        # IMPORTANT:
        # If all words were stopwords, keep original words.
        #
        # Example:
        # "how are you"
        #
        # NLTK may remove:
        # how, are, you
        #
        # Without this fallback the result becomes empty.
        # ----------------------------------------------------

        if not cleaned_tokens:

            cleaned_tokens = [
                self.lemmatizer.lemmatize(word)
                for word in tokens
            ]

        # ----------------------------------------------------
        # 6. Convert tokens back into text
        # ----------------------------------------------------

        return " ".join(cleaned_tokens)

    # ========================================================
    # GET CHATBOT RESPONSE
    # ========================================================

    def get_response(self, user_input):

        # ----------------------------------------------------
        # Check empty input
        # ----------------------------------------------------

        if not user_input or not user_input.strip():

            return {
                "response": "Please enter a question.",
                "confidence": 0,
                "intent": "empty"
            }

        # ----------------------------------------------------
        # Preprocess user's question
        # ----------------------------------------------------

        cleaned_input = self.preprocess(user_input)

        # ----------------------------------------------------
        # Check if preprocessing produced empty text
        # ----------------------------------------------------

        if not cleaned_input:

            return {
                "response": "I'm sorry, I couldn't process your question.",
                "confidence": 0,
                "intent": "unknown"
            }

        # ----------------------------------------------------
        # Convert user question into TF-IDF vector
        # ----------------------------------------------------

        user_vector = self.vectorizer.transform(
            [cleaned_input]
        )

        # ----------------------------------------------------
        # Calculate cosine similarity
        # ----------------------------------------------------

        similarities = cosine_similarity(
            user_vector,
            self.tfidf_matrix
        )[0]

        # ----------------------------------------------------
        # Find highest similarity score
        # ----------------------------------------------------

        best_match_index = similarities.argmax()

        highest_score = float(
            similarities[best_match_index]
        )

        # ----------------------------------------------------
        # Get matching intent
        # ----------------------------------------------------

        best_tag = self.tags[best_match_index]

        # ----------------------------------------------------
        # Check similarity threshold
        # ----------------------------------------------------

        if highest_score >= self.threshold:

            # Get possible responses
            possible_responses = self.responses[
                best_match_index
            ]

            # Select random response
            response = random.choice(
                possible_responses
            )

            return {
                "response": response,
                "confidence": round(highest_score, 2),
                "intent": best_tag
            }

        # ----------------------------------------------------
        # No good match:
        # Use default intent
        # ----------------------------------------------------

        default_response = (
            "Sorry, I don't understand that yet. "
            "Could you rephrase your question?"
        )

        # Search for default intent
        for intent in self.intents:

            if intent["tag"] == "default":

                default_response = random.choice(
                    intent["responses"]
                )

                break

        # ----------------------------------------------------
        # Return default response
        # ----------------------------------------------------

        return {
            "response": default_response,
            "confidence": round(highest_score, 2),
            "intent": "default"
        }