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
            "hey rulebot",
            "hello chatbot",
            "hi chatbot",
            "hey chatbot",
            "greetings",
            "hi there rulebot",
            "hello there rulebot"
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
            "how do you feel",
            "are you fine",
            "are you doing okay",
            "how have you been",
            "how is everything going",
            "are you good",
            "how are things going"
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
            "what is the name of this chatbot",
            "what is the chatbot name",
            "what should I call you",
            "what can I call you",
            "tell me your name",
            "tell me the name of the chatbot",
            "who are you",
            "who is rulebot",
            "what is rulebot",
            "what are you",
            "are you rulebot",
            "is this rulebot",
            "tell me about yourself",
            "introduce yourself",
            "can you introduce yourself"
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
            "what can rulebot do",
            "what can this chatbot do",
            "what are your capabilities",
            "what are rulebot's capabilities",
            "what can you help me with",
            "how can you help me",
            "what do you help with",
            "what questions can you answer",
            "what kind of questions can I ask",
            "what topics can you answer",
            "what topics do you support",
            "what services do you provide",
            "what are you able to do",
            "what features do you have",
            "what functions do you provide",
            "tell me your capabilities",
            "tell me what you can do",
            "what can I ask you"
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
            "how does the chatbot work",
            "explain how rulebot works",
            "explain how you work",
            "how do you answer questions",
            "how does rulebot answer questions",
            "how do you understand questions",
            "how do you understand my message",
            "how does rulebot understand messages",
            "how do you find answers",
            "how does the system work",
            "explain the working of rulebot",
            "explain your working",
            "how does your nlp work",
            "how does your question matching work",
            "how do you match user questions",
            "how do you select an answer",
            "how do you choose a response"
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
            "who built rulebot",
            "who programmed rulebot",
            "who is the developer of rulebot",
            "who is the creator of rulebot",
            "who is the programmer of rulebot",
            "who developed this chatbot",
            "who created this chatbot",
            "tell me about your developer",
            "tell me about your creator",
            "developer of rulebot",
            "creator of rulebot"
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
            "what technologies are you built with",
            "what tools do you use",
            "what programming language do you use",
            "what programming languages do you use",
            "what is your technology stack",
            "what is your tech stack",
            "what technologies are used in rulebot",
            "what technologies are used in this chatbot",
            "what software do you use",
            "what framework do you use",
            "what libraries do you use",
            "what python libraries do you use",
            "what technology powers rulebot",
            "what is rulebot built with",
            "what is this chatbot built with",
            "which technologies does rulebot use",
            "which tools were used to build rulebot",
            "tell me about your technology",
            "tell me about your tech stack"
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
            "what is the purpose of rulebot",
            "what is the purpose of this chatbot",
            "what is rulebot designed for",
            "what is this chatbot designed for",
            "why were you created",
            "why was rulebot created",
            "why was this chatbot created",
            "why do you exist",
            "why does rulebot exist",
            "what are you designed for",
            "what is your goal",
            "what is the goal of rulebot",
            "what is the goal of this chatbot",
            "what is this chatbot used for",
            "what is rulebot used for",
            "why did you build this chatbot",
            "why was this chatbot built",
            "what problem does rulebot solve",
            "tell me your purpose",
            "tell me the purpose of rulebot"
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
            "what does nlp mean",
            "what is natural language processing",
            "what does natural language processing mean",
            "explain nlp",
            "explain natural language processing",
            "tell me about nlp",
            "tell me about natural language processing",
            "how is nlp used",
            "how is natural language processing used",
            "what is nlp used for",
            "what is natural language processing used for",
            "why is nlp important",
            "why is natural language processing important",
            "how does nlp help computers"
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
            "what does tf idf mean",
            "what does tfidf mean",
            "explain tf idf",
            "explain tfidf",
            "what is tf idf vectorization",
            "what is tfidf vectorization",
            "how does tfidf work",
            "how does tf idf work",
            "why do you use tfidf",
            "why is tfidf used",
            "why does rulebot use tfidf",
            "what does tfidf do",
            "what does tf idf do",
            "how does tfidf help rulebot",
            "how does tf idf help with matching",
            "how does tfidf convert text"
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
            "what does cosine similarity mean",
            "explain cosine similarity",
            "how does cosine similarity work",
            "why do you use cosine similarity",
            "why is cosine similarity used",
            "why does rulebot use cosine similarity",
            "what is similarity matching",
            "how do you compare questions",
            "how do you compare user questions",
            "how do you match questions",
            "how does rulebot compare questions",
            "how does rulebot match questions",
            "how does cosine similarity help rulebot",
            "how is similarity calculated",
            "what does the similarity score mean"
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
            "what does nltk mean",
            "what does nltk do",
            "explain nltk",
            "tell me about nltk",
            "why do you use nltk",
            "why is nltk used",
            "why does rulebot use nltk",
            "what is natural language toolkit",
            "what does natural language toolkit mean",
            "how is nltk used in this chatbot",
            "how does nltk help rulebot",
            "what does nltk do in rulebot",
            "what is nltk used for"
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
            "what does python mean",
            "tell me about python",
            "explain python",
            "what is python programming",
            "what is the python programming language",
            "why is python popular",
            "why is python widely used",
            "what is python used for",
            "where is python used",
            "what can python be used for",
            "why does rulebot use python",
            "why is python used in rulebot",
            "how is python used in this chatbot",
            "what are the advantages of python"
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
            "what does flask mean",
            "tell me about flask",
            "explain flask",
            "what is flask framework",
            "what is the flask framework",
            "why do you use flask",
            "why is flask used",
            "why does rulebot use flask",
            "what is flask used for",
            "how is flask used in this chatbot",
            "how does flask help rulebot",
            "what does flask do in this chatbot",
            "what can flask be used for"
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
            "what does artificial intelligence mean",
            "what is ai",
            "what does ai mean",
            "tell me about ai",
            "tell me about artificial intelligence",
            "explain ai",
            "explain artificial intelligence",
            "how does artificial intelligence work",
            "how does ai work",
            "what is artificial intelligence used for",
            "what is ai used for",
            "why is artificial intelligence important",
            "why is ai important",
            "what can artificial intelligence do",
            "what can ai do"
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
            "what does machine learning mean",
            "what is ml",
            "what does ml mean",
            "tell me about machine learning",
            "explain machine learning",
            "how does machine learning work",
            "what is machine learning used for",
            "what is ml used for",
            "is machine learning ai",
            "is ml a part of ai",
            "how is machine learning related to ai",
            "why is machine learning important",
            "what can machine learning do",
            "how does machine learning learn from data"
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
            "what are stop words",
            "what is a stopword",
            "what is stopword removal",
            "what is stop word removal",
            "explain stopwords",
            "explain stop words",
            "why remove stopwords",
            "why remove stop words",
            "why do you remove stopwords",
            "why do you remove stop words",
            "how are stopwords used",
            "how are stop words used",
            "what does stopword removal do",
            "what does stop word removal do"
        ],
        "responses": [
            "Stopwords are common words that may provide little useful information for text matching. NLTK can remove them during text matching.",
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
            "what does tokenization mean",
            "explain tokenization",
            "tell me about tokenization",
            "what is tokenization in nlp",
            "what is text tokenization",
            "why do you tokenize text",
            "why is tokenization used",
            "how does tokenization work",
            "how does text tokenization work",
            "what does tokenization do",
            "how is tokenization used in this chatbot",
            "how does nltk tokenize text"
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
            "what does lemmatization mean",
            "explain lemmatization",
            "tell me about lemmatization",
            "why do you use lemmatization",
            "why is lemmatization used",
            "how does lemmatization work",
            "what does lemmatization do",
            "what is lemmatization in nlp",
            "how is lemmatization used in this chatbot",
            "why does rulebot use lemmatization",
            "how does lemmatization help text matching"
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
            "thank you very much",
            "i appreciate it",
            "i appreciate your help",
            "that was helpful",
            "this was helpful",
            "you helped me",
            "thanks for your help",
            "thanks for helping me",
            "many thanks"
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
            "i need to go",
            "i am leaving",
            "exit",
            "quit",
            "end the chat",
            "end conversation",
            "stop chatting",
            "good night",
            "see you next time"
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