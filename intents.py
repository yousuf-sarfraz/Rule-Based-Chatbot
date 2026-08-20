intents = [

    # ============================================================
    # GREETING
    # ============================================================

    {
        "tag": "greeting",
        "patterns": [
            "hello",
            "hi",
            "hey",
            "hey there",
            "hello there",
            "hi there",
            "good morning",
            "good afternoon",
            "good evening",
            "nice to meet you",
            "hello rulebot",
            "hi rulebot",
            "hey rulebot"
        ],
        "responses": [
            "👋 Hello! How can I help you today?",
            "😊 Hi there! Nice to meet you.",
            "Welcome! Ask me anything.",
            "Hello! I'm RuleBot, your virtual assistant."
        ]
    },


    # ============================================================
    # HOW ARE YOU
    # ============================================================

    {
        "tag": "how_are_you",
        "patterns": [
            "how are you",
            "how are you doing",
            "how are you today",
            "how is it going",
            "how are things",
            "are you doing well",
            "are you okay",
            "how do you feel"
        ],
        "responses": [
            "I'm doing great! Thanks for asking 😊",
            "I'm fine and ready to help!",
            "Everything is working perfectly!",
            "I'm doing well. How can I help you?"
        ]
    },


    # ============================================================
    # NAME / IDENTITY
    # ============================================================

    {
        "tag": "name",
        "patterns": [
            "what is your name",
            "what's your name",
            "tell me your name",
            "your name",
            "who are you",
            "what are you",
            "who is rulebot",
            "tell me about yourself",
            "introduce yourself"
        ],
        "responses": [
            "I'm RuleBot, your virtual assistant.",
            "My name is RuleBot.",
            "You can call me RuleBot.",
            "I'm a Python-based rule-oriented NLP chatbot."
        ]
    },


    # ============================================================
    # CAPABILITIES
    # ============================================================

    {
        "tag": "capabilities",
        "patterns": [
            "what can you do",
            "what are your capabilities",
            "what can you help me with",
            "what do you do",
            "what are you able to do",
            "what services do you provide",
            "what can rulebot do",
            "what questions can you answer",
            "how can you help me",
            "what kind of questions can i ask",
            "tell me your capabilities",
            "tell me what you can do"
        ],
        "responses": [
            "I can answer questions from my knowledge base, process your text using NLP, identify user intents, and provide relevant responses.",
            "I can chat with you, answer questions about my supported topics, recognize intents, and provide responses using TF-IDF and cosine similarity.",
            "I can answer questions about programming, AI, machine learning, Flask, Python, and information about myself.",
            "I can understand different forms of supported questions by using NLP preprocessing and text similarity."
        ]
    },


    # ============================================================
    # HOW CHATBOT WORKS
    # ============================================================

    {
        "tag": "how_i_work",
        "patterns": [
            "how do you work",
            "how does rulebot work",
            "how does this chatbot work",
            "explain how you work",
            "how do you answer questions",
            "how do you understand questions",
            "how do you understand my message",
            "how do you find answers",
            "how does the system work",
            "explain your working",
            "how does your nlp work"
        ],
        "responses": [
            "I preprocess your message with NLTK, convert it into TF-IDF features, compare it with stored patterns using cosine similarity, and select the most relevant response.",
            "When you send a message, I clean and process the text, compare it with my stored patterns using TF-IDF and cosine similarity, and return the best matching response.",
            "I use Natural Language Processing, TF-IDF vectorization, and cosine similarity to find the pattern that is most similar to your question."
        ]
    },


    # ============================================================
    # CREATOR / DEVELOPER
    # ============================================================

    {
        "tag": "creator",
        "patterns": [
            "who made you",
            "who created you",
            "who built you",
            "who developed you",
            "who is your developer",
            "who is your creator",
            "who programmed you",
            "who designed you",
            "who developed rulebot",
            "who created rulebot",
            "who made rulebot",
            "tell me about your developer",
            "developer of rulebot"
        ],
        "responses": [
            "I was developed by Yousuf Sarfraz using Python, Flask, NLTK, and Scikit-learn.",
            "I was built by Yousuf Sarfraz as a Python-based NLP chatbot project.",
            "My developer is Yousuf Sarfraz. I was created using Python, Flask, NLTK, and machine-learning techniques such as TF-IDF and cosine similarity."
        ]
    },


    # ============================================================
    # TECHNOLOGY
    # ============================================================

    {
        "tag": "technology",
        "patterns": [
            "what technology do you use",
            "what technologies do you use",
            "what technology are you built with",
            "what tools do you use",
            "what programming language do you use",
            "what is your technology",
            "what technologies are used",
            "what software do you use",
            "what framework do you use",
            "what libraries do you use",
            "what is your tech stack",
            "tell me about your technology"
        ],
        "responses": [
            "I use Python, Flask, NLTK, and Scikit-learn. My NLP system uses TF-IDF vectorization and cosine similarity for question matching.",
            "My main technologies are Python and Flask. For Natural Language Processing, I use NLTK, and for text similarity I use Scikit-learn.",
            "I am built with Python and Flask, with NLTK for text preprocessing and Scikit-learn for TF-IDF and cosine similarity."
        ]
    },


    # ============================================================
    # PURPOSE
    # ============================================================

    {
        "tag": "purpose",
        "patterns": [
            "what is your purpose",
            "why were you created",
            "what is the purpose of rulebot",
            "why do you exist",
            "what are you designed for",
            "what is your goal",
            "why was rulebot created",
            "what is the goal of this chatbot",
            "what is this chatbot used for",
            "what is the purpose of this chatbot",
            "why did you build this chatbot",
            "tell me your purpose"
        ],
        "responses": [
            "My purpose is to demonstrate how a Python-based NLP chatbot can understand user questions and provide relevant responses.",
            "I was designed as an educational NLP chatbot project to demonstrate intent recognition, text preprocessing, TF-IDF, cosine similarity, and Flask web development.",
            "My goal is to provide a simple conversational interface while demonstrating how Natural Language Processing and text similarity can be used to build a chatbot."
        ]
    },


    # ============================================================
    # NLP
    # ============================================================

    {
        "tag": "nlp",
        "patterns": [
            "what is nlp",
            "what is natural language processing",
            "explain nlp",
            "tell me about nlp",
            "what does nlp mean",
            "how is nlp used",
            "what is natural language processing used for"
        ],
        "responses": [
            "NLP stands for Natural Language Processing. It is a field of AI that helps computers process and understand human language.",
            "Natural Language Processing allows computers to work with human language such as text and speech.",
            "In this chatbot, NLTK is used for text preprocessing such as tokenization, stopword removal, and lemmatization."
        ]
    },


    # ============================================================
    # TF-IDF
    # ============================================================

    {
        "tag": "tfidf",
        "patterns": [
            "what is tf idf",
            "what is tfidf",
            "explain tfidf",
            "what is tf idf vectorization",
            "how does tfidf work",
            "why do you use tfidf",
            "what does tfidf do"
        ],
        "responses": [
            "TF-IDF stands for Term Frequency-Inverse Document Frequency. It converts text into numerical features based on the importance of words.",
            "I use TF-IDF to convert user questions and stored patterns into numerical vectors so they can be compared.",
            "TF-IDF helps identify which words are important in a piece of text."
        ]
    },


    # ============================================================
    # COSINE SIMILARITY
    # ============================================================

    {
        "tag": "cosine_similarity",
        "patterns": [
            "what is cosine similarity",
            "explain cosine similarity",
            "how does cosine similarity work",
            "why do you use cosine similarity",
            "what is similarity matching",
            "how do you compare questions",
            "how do you match questions"
        ],
        "responses": [
            "Cosine similarity measures how similar two text vectors are. I use it to compare your question with my stored patterns.",
            "I use cosine similarity after TF-IDF vectorization to find the pattern that is most similar to your question.",
            "Cosine similarity produces a similarity score that helps me select the most relevant intent."
        ]
    },


    # ============================================================
    # NLTK
    # ============================================================

    {
        "tag": "nltk",
        "patterns": [
            "what is nltk",
            "what does nltk do",
            "why do you use nltk",
            "explain nltk",
            "what is natural language toolkit",
            "how is nltk used in this chatbot"
        ],
        "responses": [
            "NLTK stands for Natural Language Toolkit. It is a Python library used for Natural Language Processing.",
            "I use NLTK for tokenization, stopword removal, and lemmatization during text preprocessing."
        ]
    },


    # ============================================================
    # PYTHON
    # ============================================================

    {
        "tag": "python",
        "patterns": [
            "what is python",
            "tell me about python",
            "explain python",
            "what is python programming",
            "why is python popular",
            "what is python used for",
            "where is python used"
        ],
        "responses": [
            "Python is a powerful programming language used in AI, web development, automation, data science, and many other fields.",
            "Python is a high-level programming language known for its readable syntax and large collection of libraries."
        ]
    },


    # ============================================================
    # FLASK
    # ============================================================

    {
        "tag": "flask",
        "patterns": [
            "what is flask",
            "tell me about flask",
            "explain flask",
            "what is flask framework",
            "why do you use flask",
            "what is flask used for",
            "how is flask used in this chatbot"
        ],
        "responses": [
            "Flask is a lightweight Python web framework used to build web applications and APIs.",
            "This chatbot uses Flask to connect the Python chatbot logic with the web interface."
        ]
    },


    # ============================================================
    # ARTIFICIAL INTELLIGENCE
    # ============================================================

    {
        "tag": "ai",
        "patterns": [
            "what is artificial intelligence",
            "what is ai",
            "tell me about ai",
            "explain artificial intelligence",
            "explain ai",
            "what does ai mean",
            "how does artificial intelligence work"
        ],
        "responses": [
            "Artificial Intelligence is a field of computer science focused on creating systems that can perform tasks that normally require human intelligence.",
            "AI enables computers to perform tasks such as learning, reasoning, recognizing patterns, and understanding language."
        ]
    },


    # ============================================================
    # MACHINE LEARNING
    # ============================================================

    {
        "tag": "machine_learning",
        "patterns": [
            "what is machine learning",
            "what is ml",
            "tell me about machine learning",
            "explain machine learning",
            "what does machine learning mean",
            "how does machine learning work",
            "is machine learning ai"
        ],
        "responses": [
            "Machine Learning is a branch of AI where computers learn patterns from data and use those patterns to make predictions or decisions.",
            "Machine Learning allows computer systems to improve their performance by learning from data."
        ]
    },


    # ============================================================
    # STOPWORDS
    # ============================================================

    {
        "tag": "stopwords",
        "patterns": [
            "what are stopwords",
            "what is stopword removal",
            "why remove stopwords",
            "why do you remove stopwords",
            "how are stopwords used"
        ],
        "responses": [
            "Stopwords are common words that may provide little useful information for text matching. NLTK can remove them during preprocessing.",
            "My preprocessing uses an English stopword list to reduce unnecessary words before text matching."
        ]
    },


    # ============================================================
    # TOKENIZATION
    # ============================================================

    {
        "tag": "tokenization",
        "patterns": [
            "what is tokenization",
            "what is tokenization in nlp",
            "explain tokenization",
            "why do you tokenize text",
            "how does tokenization work"
        ],
        "responses": [
            "Tokenization breaks text into smaller units called tokens, usually words or sentences. This chatbot uses NLTK word tokenization."
        ]
    },


    # ============================================================
    # LEMMATIZATION
    # ============================================================

    {
        "tag": "lemmatization",
        "patterns": [
            "what is lemmatization",
            "explain lemmatization",
            "hy do you use lemmatization",
            "what does lemmatization do",
            "how does lemmatization work"
        ],
        "responses": [
            "Lemmatization reduces words to their base or dictionary form. This helps similar words match more effectively during text processing."
        ]
    },


    # ============================================================
    # THANKS
    # ============================================================

    {
        "tag": "thanks",
        "patterns": [
            "thank you",
            "thanks",
            "thankyou",
            "thanks a lot",
            "thank you so much",
            "i appreciate it",
            "that was helpful"
        ],
        "responses": [
            "You're welcome! 😊",
            "Happy to help!",
            "Anytime! 😊",
            "Glad I could help!"
        ]
    },


    # ============================================================
    # GOODBYE
    # ============================================================

    {
        "tag": "goodbye",
        "patterns": [
            "bye",
            "goodbye",
            "see you",
            "see you later",
            "talk to you later",
            "i have to go",
            "exit",
            "quit"
        ],
        "responses": [
            "👋 Goodbye!",
            "Take care!",
            "Have a wonderful day!",
            "Goodbye! Thanks for chatting with me."
        ]
    },


    # ============================================================
    # DEFAULT / UNKNOWN
    # ============================================================

    {
        "tag": "default",
        "patterns": [],
        "responses": [
            "Sorry, I don't understand that yet. Could you rephrase your question?",
            "I'm not sure I understand. Try asking me about my capabilities, technology, NLP, Python, Flask, AI, or machine learning.",
            "I don't have an answer for that yet. Please try another question.",
            "I'm still learning. Please ask me something related to my supported topics."
        ]
    }

]