// ===============================
// RuleBot JavaScript
// ===============================

const inputField = document.getElementById("message");
const chatArea = document.getElementById("chat-area");

// Send message when Enter is pressed
inputField.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

// Add message to chat
function addMessage(message, sender) {

    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message");
    messageDiv.classList.add(sender);

    messageDiv.innerHTML = `
        <div>${message}</div>
        <small>${getCurrentTime()}</small>
    `;

    chatArea.appendChild(messageDiv);

    scrollToBottom();
}

// Get current time
function getCurrentTime() {

    const now = new Date();

    return now.toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });

}

// Typing animation
function showTyping() {

    const typing = document.createElement("div");

    typing.classList.add("message");
    typing.classList.add("bot");

    typing.id = "typing";

    typing.innerHTML = `
        <div class="typing">
            <span></span>
            <span></span>
            <span></span>
        </div>
    `;

    chatArea.appendChild(typing);

    scrollToBottom();

}

// Remove typing animation
function removeTyping() {

    const typing = document.getElementById("typing");

    if (typing) {
        typing.remove();
    }

}

// Scroll chat automatically
function scrollToBottom() {

    chatArea.scrollTop = chatArea.scrollHeight;

}

// Main function
function sendMessage() {

    const message = inputField.value.trim();

    if (message === "") return;

    addMessage(message, "user");

    inputField.value = "";

    showTyping();

    fetch("/get", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })

    })

    .then(response => response.json())

    .then(data => {

        removeTyping();

        addMessage(data.response, "bot");

    })

    .catch(error => {

        removeTyping();

        addMessage(
            "⚠️ Sorry! Something went wrong. Please try again.",
            "bot"
        );

        console.error(error);

    });

}

// Focus input when page loads
window.onload = () => {

    inputField.focus();

};