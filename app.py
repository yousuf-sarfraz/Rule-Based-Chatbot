from flask import Flask, render_template, request, jsonify

from chatbot import FAQChatbot
from intents import intents


# ============================================================
# CREATE FLASK APPLICATION
# ============================================================

app = Flask(__name__)


# ============================================================
# INITIALIZE CHATBOT
# ============================================================

bot = FAQChatbot(intents)


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


# ============================================================
# CHAT API
# ============================================================

@app.route("/get", methods=["POST"])
def chat():

    # --------------------------------------------------------
    # Get JSON data
    # --------------------------------------------------------

    data = request.get_json(silent=True)

    # --------------------------------------------------------
    # Validate request
    # --------------------------------------------------------

    if not data or not isinstance(data, dict):

        return jsonify({
            "response": "Invalid request.",
            "confidence": 0,
            "intent": "error"
        }), 400

    # --------------------------------------------------------
    # Get user message
    # --------------------------------------------------------

    message = data.get("message", "")

    # Make sure message is a string
    if not isinstance(message, str):

        return jsonify({
            "response": "Message must be text.",
            "confidence": 0,
            "intent": "error"
        }), 400

    message = message.strip()

    # --------------------------------------------------------
    # Check empty message
    # --------------------------------------------------------

    if not message:

        return jsonify({
            "response": "Please enter a message.",
            "confidence": 0,
            "intent": "empty"
        }), 400

    # --------------------------------------------------------
    # Get chatbot response
    # --------------------------------------------------------

    result = bot.get_response(message)

    # --------------------------------------------------------
    # Return chatbot result
    # --------------------------------------------------------

    return jsonify(result)


# ============================================================
# 404 ERROR HANDLER
# ============================================================

@app.errorhandler(404)
def not_found(error):

    return render_template("index.html"), 404


# ============================================================
# 405 METHOD NOT ALLOWED
# ============================================================

@app.errorhandler(405)
def method_not_allowed(error):

    return jsonify({
        "response": "Method not allowed.",
        "confidence": 0,
        "intent": "error"
    }), 405


# ============================================================
# 500 INTERNAL SERVER ERROR
# ============================================================

@app.errorhandler(500)
def server_error(error):

    return jsonify({
        "response": "Internal server error.",
        "confidence": 0,
        "intent": "error"
    }), 500


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )