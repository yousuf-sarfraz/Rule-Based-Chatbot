# 🤖 RuleBot - NLP Rule-Based Chatbot

A modern and interactive **Rule-Based NLP Chatbot** built with **Python, Flask, NLTK, and Scikit-learn**.

RuleBot uses **Natural Language Processing (NLP)** to preprocess user messages and **TF-IDF with cosine similarity** to identify the most relevant intent and return an appropriate response.

This project is designed as an educational chatbot project demonstrating how NLP techniques can be combined with a Flask web application.

---

## 📌 Features

- 🤖 Rule-Based Chatbot
- 🧠 Natural Language Processing (NLP)
- 🔤 Text Tokenization using NLTK
- 🛑 Stopword Removal
- 🌱 Word Lemmatization
- 📊 TF-IDF Vectorization
- 📐 Cosine Similarity
- 🎯 Intent Recognition
- 📈 Confidence Score
- 💬 Predefined Intent Responses
- 🎲 Random Response Selection
- 🌐 Flask Web Application
- 🎨 Modern Responsive User Interface
- 📱 Mobile-Friendly Design
- ⌨️ Interactive Chat Input
- ⏳ Typing Indicator
- 📜 Automatic Chat Scrolling
- 🛡️ Input Validation
- ⚠️ Error Handling
- 🧩 Easy to Extend with New Intents

---

## 🧠 How RuleBot Works

RuleBot follows an NLP-based text matching process.

```text
User Message
     │
     ▼
Text Preprocessing
     │
     ├── Lowercase Conversion
     ├── Punctuation Removal
     ├── Tokenization
     ├── Stopword Removal
     └── Lemmatization
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Cosine Similarity
     │
     ▼
Best Matching Pattern
     │
     ▼
Intent Recognition
     │
     ▼
Confidence Check
     │
     ├── Good Match
     │      │
     │      ▼
     │   Response
     │
     └── Poor Match
            │
            ▼
       Default Response