intents = [

{
    "tag":"greeting",
    "patterns":[
        "hello",
        "hi",
        "hey",
        "good morning",
        "good evening",
        "good afternoon"
    ],
    "responses":[
        "👋 Hello! How can I help you today?",
        "😊 Hi there! Nice to meet you.",
        "Welcome! Ask me anything.",
        "Hello! I'm your Rule-Based Chatbot."
    ]
},

{
    "tag":"how_are_you",
    "patterns":[
        "how are you",
        "how are u"
    ],
    "responses":[
        "I'm doing great! Thanks for asking 😊",
        "I'm fine. Hope you're having a wonderful day!",
        "Everything is working perfectly!"
    ]
},

{
    "tag":"name",
    "patterns":[
        "your name",
        "who are you",
        "what is your name"
    ],
    "responses":[
        "I'm RuleBot, your virtual assistant.",
        "My name is RuleBot.",
        "You can call me RuleBot."
    ]
},

{
    "tag":"python",
    "patterns":[
        "python",
        "what is python"
    ],
    "responses":[
        "Python is a powerful programming language used in AI, web development, automation, and data science."
    ]
},

{
    "tag":"flask",
    "patterns":[
        "flask",
        "what is flask"
    ],
    "responses":[
        "Flask is a lightweight Python web framework used to build web applications."
    ]
},

{
    "tag":"ai",
    "patterns":[
        "artificial intelligence",
        "ai",
        "what is ai"
    ],
    "responses":[
        "Artificial Intelligence enables machines to learn, reason, and solve problems like humans."
    ]
},

{
    "tag":"machine learning",
    "patterns":[
        "machine learning",
        "ml"
    ],
    "responses":[
        "Machine Learning is a branch of AI where computers learn from data."
    ]
},

{
    "tag":"creator",
    "patterns":[
        "who made you",
        "who created you",
        "developer"
    ],
    "responses":[
        "I was developed by Yousuf Sarfraz using Python and Flask."
    ]
},

{
    "tag":"thanks",
    "patterns":[
        "thank you",
        "thanks",
        "thankyou"
    ],
    "responses":[
        "You're welcome! 😊",
        "Happy to help!",
        "Anytime!"
    ]
},

{
    "tag":"goodbye",
    "patterns":[
        "bye",
        "goodbye",
        "see you"
    ],
    "responses":[
        "👋 Goodbye!",
        "Take care!",
        "Have a wonderful day!"
    ]
},

{
    "tag":"default",
    "patterns":[],
    "responses":[
        "Sorry, I don't understand that yet.",
        "Could you rephrase your question?",
        "I'm still learning. Please ask something else.",
        "I don't have an answer for that."
    ]
}

]