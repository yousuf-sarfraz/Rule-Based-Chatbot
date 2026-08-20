// ============================================================
// RuleBot JavaScript
// ============================================================


// ============================================================
// GET HTML ELEMENTS
// ============================================================

const inputField = document.getElementById("message");
const chatArea = document.getElementById("chat-area");
const chatForm = document.getElementById("chat-form");
const sendButton = document.getElementById("send-button");
const typingIndicator = document.getElementById("typing-indicator");


// ============================================================
// CHECK REQUIRED ELEMENTS
// ============================================================

if (!inputField || !chatArea || !chatForm || !sendButton) {

    console.error(
        "RuleBot: Required HTML elements were not found."
    );

}


// ============================================================
// FORM SUBMISSION
// ============================================================

chatForm.addEventListener("submit", function (event) {

    // Prevent page refresh
    event.preventDefault();

    sendMessage();

});


// ============================================================
// ADD MESSAGE TO CHAT
// ============================================================

function addMessage(
    message,
    sender,
    confidence = null,
    intent = null
) {

    const messageDiv = document.createElement("div");

    messageDiv.classList.add(
        "message",
        sender
    );


    // --------------------------------------------------------
    // Sender name
    // --------------------------------------------------------

    const senderElement = document.createElement("span");

    senderElement.classList.add(
        "message-sender"
    );

    senderElement.textContent =
        sender === "user"
            ? "You"
            : "RuleBot";


    // --------------------------------------------------------
    // Message content
    // --------------------------------------------------------

    const contentDiv = document.createElement("div");

    contentDiv.classList.add(
        "message-content"
    );

    // textContent prevents HTML injection
    contentDiv.textContent = message;


    // --------------------------------------------------------
    // Time
    // --------------------------------------------------------

    const timeElement = document.createElement("small");

    timeElement.classList.add(
        "message-time"
    );

    timeElement.textContent =
        getCurrentTime();


    // --------------------------------------------------------
    // Add sender
    // --------------------------------------------------------

    messageDiv.appendChild(
        senderElement
    );


    // --------------------------------------------------------
    // Add content
    // --------------------------------------------------------

    messageDiv.appendChild(
        contentDiv
    );


    // --------------------------------------------------------
    // Add chatbot information
    // --------------------------------------------------------

    if (
        sender === "bot" &&
        typeof confidence === "number" &&
        intent
    ) {

        const infoElement =
            document.createElement("small");

        infoElement.classList.add(
            "bot-info"
        );


        const percentage =
            Math.round(
                confidence * 100
            );


        infoElement.textContent =
            `Intent: ${formatIntent(intent)} | Confidence: ${percentage}%`;


        messageDiv.appendChild(
            infoElement
        );

    }


    // --------------------------------------------------------
    // Add time
    // --------------------------------------------------------

    messageDiv.appendChild(
        timeElement
    );


    // --------------------------------------------------------
    // Add message to chat
    // --------------------------------------------------------

    chatArea.appendChild(
        messageDiv
    );


    // Scroll to latest message
    scrollToBottom();

}


// ============================================================
// FORMAT INTENT NAME
// ============================================================

function formatIntent(intent) {

    if (!intent) {
        return "Unknown";
    }


    return intent
        .replace(/_/g, " ")
        .replace(/\b\w/g, function (letter) {
            return letter.toUpperCase();
        });

}


// ============================================================
// GET CURRENT TIME
// ============================================================

function getCurrentTime() {

    const now = new Date();

    return now.toLocaleTimeString([], {

        hour: "2-digit",

        minute: "2-digit"

    });

}


// ============================================================
// SHOW TYPING INDICATOR
// ============================================================

function showTyping() {

    if (!typingIndicator) {
        return;
    }


    typingIndicator.classList.add(
        "active"
    );


    typingIndicator.setAttribute(
        "aria-hidden",
        "false"
    );


    scrollToBottom();

}


// ============================================================
// REMOVE TYPING INDICATOR
// ============================================================

function removeTyping() {

    if (!typingIndicator) {
        return;
    }


    typingIndicator.classList.remove(
        "active"
    );


    typingIndicator.setAttribute(
        "aria-hidden",
        "true"
    );

}


// ============================================================
// SCROLL CHAT TO BOTTOM
// ============================================================

function scrollToBottom() {

    chatArea.scrollTo({

        top: chatArea.scrollHeight,

        behavior: "smooth"

    });

}


// ============================================================
// SET INPUT STATE
// ============================================================

function setInputState(disabled) {

    inputField.disabled = disabled;

    sendButton.disabled = disabled;


    if (disabled) {

        sendButton.setAttribute(
            "aria-busy",
            "true"
        );

    } else {

        sendButton.removeAttribute(
            "aria-busy"
        );

    }

}


// ============================================================
// SEND MESSAGE
// ============================================================

async function sendMessage() {

    const message =
        inputField.value.trim();


    // --------------------------------------------------------
    // Don't send empty message
    // --------------------------------------------------------

    if (!message) {

        inputField.focus();

        return;

    }


    // --------------------------------------------------------
    // Prevent very long messages
    // --------------------------------------------------------

    if (message.length > 500) {

        addMessage(
            "⚠️ Your message is too long. Please keep it under 500 characters.",
            "bot"
        );

        return;

    }


    // --------------------------------------------------------
    // Disable input
    // --------------------------------------------------------

    setInputState(true);


    // --------------------------------------------------------
    // Display user's message
    // --------------------------------------------------------

    addMessage(
        message,
        "user"
    );


    // --------------------------------------------------------
    // Clear input
    // --------------------------------------------------------

    inputField.value = "";


    // --------------------------------------------------------
    // Show typing indicator
    // --------------------------------------------------------

    showTyping();


    try {

        // ====================================================
        // SEND REQUEST TO FLASK
        // ====================================================

        const response =
            await fetch("/get", {

                method: "POST",

                headers: {

                    "Content-Type":
                        "application/json",

                    "Accept":
                        "application/json"

                },

                body: JSON.stringify({

                    message: message

                })

            });


        // ====================================================
        // READ RESPONSE
        // ====================================================

        let data;


        try {

            data =
                await response.json();

        } catch (jsonError) {

            throw new Error(
                "Server returned an invalid JSON response."
            );

        }


        // ====================================================
        // CHECK HTTP STATUS
        // ====================================================

        if (!response.ok) {

            throw new Error(
                data.response ||
                `Server returned ${response.status}`
            );

        }


        // ====================================================
        // VALIDATE CHATBOT RESPONSE
        // ====================================================

        if (
            !data ||
            typeof data.response !== "string"
        ) {

            throw new Error(
                "Invalid chatbot response."
            );

        }


        // ====================================================
        // REMOVE TYPING INDICATOR
        // ====================================================

        removeTyping();


        // ====================================================
        // DISPLAY CHATBOT RESPONSE
        // ====================================================

        addMessage(

            data.response,

            "bot",

            typeof data.confidence === "number"
                ? data.confidence
                : null,

            data.intent || null

        );


    } catch (error) {

        // ----------------------------------------------------
        // Remove typing indicator
        // ----------------------------------------------------

        removeTyping();


        // ----------------------------------------------------
        // Show error message
        // ----------------------------------------------------

        addMessage(

            "⚠️ Sorry! I couldn't connect to the chatbot. Please try again.",

            "bot"

        );


        // ----------------------------------------------------
        // Log error for developer
        // ----------------------------------------------------

        console.error(
            "RuleBot error:",
            error
        );

    } finally {

        // ----------------------------------------------------
        // Enable input
        // ----------------------------------------------------

        setInputState(false);


        // ----------------------------------------------------
        // Focus input
        // ----------------------------------------------------

        inputField.focus();

    }

}


// ============================================================
// PAGE LOAD
// ============================================================

window.addEventListener(
    "load",
    function () {

        inputField.focus();

    }
);