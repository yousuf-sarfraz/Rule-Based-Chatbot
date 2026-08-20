import re
import random
import nltk

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# DOWNLOAD REQUIRED NLTK RESOURCES
# ============================================================

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
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

        # ----------------------------------------------------
        # Store intents
        # ----------------------------------------------------

        self.intents = intents

        # ----------------------------------------------------
        # Create pattern data
        # ----------------------------------------------------

        self.patterns = []
        self.responses = []
        self.tags = []

        # ----------------------------------------------------
        # Extract patterns, responses and tags
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
        #
        # 1,2,3 means:
        #   single words
        #   two-word phrases
        #   three-word phrases
        #
        # This gives more importance to complete phrases.
        # ----------------------------------------------------

        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 3),
            sublinear_tf=True
        )

        # ----------------------------------------------------
        # Convert patterns into TF-IDF vectors
        # ----------------------------------------------------

        self.tfidf_matrix = self.vectorizer.fit_transform(
            self.cleaned_patterns
        )

        # ----------------------------------------------------
        # Matching configuration
        # ----------------------------------------------------

        # Minimum similarity required for a match.
        self.threshold = 0.45

        # Difference required between the best and second-best
        # match when the result is not an exact match.
        self.margin_threshold = 0.08

    # ========================================================
    # TEXT PREPROCESSING
    # ========================================================

    def preprocess(self, text):

        # ----------------------------------------------------
        # 1. Convert to lowercase
        # ----------------------------------------------------

        text = text.lower().strip()

        # ----------------------------------------------------
        # 2. Remove punctuation
        # ----------------------------------------------------

        text = re.sub(r"[^\w\s]", " ", text)

        # ----------------------------------------------------
        # 3. Tokenize
        # ----------------------------------------------------

        tokens = word_tokenize(text)

        # ----------------------------------------------------
        # 4. Lemmatize
        #
        # IMPORTANT:
        # We DO NOT remove stopwords here.
        #
        # Words such as:
        # "what", "is", "your", "who", "are"
        #
        # can be important for distinguishing intents.
        # ----------------------------------------------------

        cleaned_tokens = [
            self.lemmatizer.lemmatize(word)
            for word in tokens
        ]

        # ----------------------------------------------------
        # 5. Convert tokens back into text
        # ----------------------------------------------------

        return " ".join(cleaned_tokens)

    # ========================================================
    # EXACT MATCH
    # ========================================================

    def find_exact_match(self, user_input):

        cleaned_input = self.preprocess(user_input)

        for index, pattern in enumerate(self.cleaned_patterns):

            if cleaned_input == pattern:

                return index

        return None

    # ========================================================
    # DEFAULT RESPONSE
    # ========================================================

    def get_default_response(self):

        default_response = (
            "Sorry, I don't understand that yet. "
            "Could you rephrase your question?"
        )

        for intent in self.intents:

            if intent["tag"] == "default":

                default_response = random.choice(
                    intent["responses"]
                )

                break

        return default_response

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
        # Preprocess user input
        # ----------------------------------------------------

        cleaned_input = self.preprocess(user_input)

        # ----------------------------------------------------
        # Check preprocessing result
        # ----------------------------------------------------

        if not cleaned_input:

            return {
                "response": self.get_default_response(),
                "confidence": 0,
                "intent": "default"
            }

        # ====================================================
        # STEP 1: EXACT MATCH
        # ====================================================

        exact_match_index = self.find_exact_match(user_input)

        if exact_match_index is not None:

            possible_responses = self.responses[
                exact_match_index
            ]

            return {
                "response": random.choice(
                    possible_responses
                ),
                "confidence": 1.0,
                "intent": self.tags[exact_match_index]
            }

        # ====================================================
        # STEP 2: TF-IDF MATCHING
        # ====================================================

        user_vector = self.vectorizer.transform(
            [cleaned_input]
        )

        similarities = cosine_similarity(
            user_vector,
            self.tfidf_matrix
        )[0]

        # ----------------------------------------------------
        # Get best and second-best matches
        # ----------------------------------------------------

        ranked_indices = similarities.argsort()[::-1]

        best_match_index = ranked_indices[0]

        highest_score = float(
            similarities[best_match_index]
        )

        # ----------------------------------------------------
        # Get second-best score
        # ----------------------------------------------------

        if len(ranked_indices) > 1:

            second_best_index = ranked_indices[1]

            second_best_score = float(
                similarities[second_best_index]
            )

        else:

            second_best_score = 0.0

        # ----------------------------------------------------
        # Calculate difference between top matches
        # ----------------------------------------------------

        score_margin = (
            highest_score - second_best_score
        )

        # ====================================================
        # STEP 3: CHECK WHETHER MATCH IS STRONG ENOUGH
        # ====================================================

        if highest_score < self.threshold:

            return {
                "response": self.get_default_response(),
                "confidence": round(
                    highest_score,
                    2
                ),
                "intent": "default"
            }

        # ----------------------------------------------------
        # If two intents are almost equally similar,
        # don't make a risky prediction.
        # ----------------------------------------------------

        if score_margin < self.margin_threshold:

            return {
                "response": self.get_default_response(),
                "confidence": round(
                    highest_score,
                    2
                ),
                "intent": "default"
            }

        # ====================================================
        # STEP 4: RETURN BEST MATCH
        # ====================================================

        best_tag = self.tags[best_match_index]

        possible_responses = self.responses[
            best_match_index
        ]

        response = random.choice(
            possible_responses
        )

        return {
            "response": response,
            "confidence": round(
                highest_score,
                2
            ),
            "intent": best_tag
        }