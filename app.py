from flask import Flask, render_template, request, jsonify
from chatbot import RuleBasedChatbot

app = Flask(__name__)

bot = RuleBasedChatbot()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chat():
    data = request.get_json()

    if not data:
        return jsonify({"response": "Invalid request."})

    message = data.get("message", "").strip()

    if not message:
        return jsonify({"response": "Please enter a message."})

    response = bot.get_response(message)

    return jsonify({"response": response})


@app.errorhandler(404)
def not_found(error):
    return render_template("index.html"), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({"response": "Internal Server Error"}), 500


if __name__ == "__main__":
    app.run(debug=True)