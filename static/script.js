// --- Imports/Setup (Keep these as they are) ---
const chatWindow = document.getElementById('chat-window');
const userInput = document.getElementById('user-input');
// ... (Keep the rest of your timer variable declarations as they are) ...

// --- Chatbot Functions (MODIFIED) ---

function sendMessage() {
    const messageText = userInput.value.trim();
    if (messageText === '') return;

    appendMessage(messageText, 'user-message');
    // Call the new function to use the Python backend
    sendToServer(messageText); 
    userInput.value = '';
}

// *** NEW FUNCTION TO COMMUNICATE WITH PYTHON FLASK SERVER ***
async function sendToServer(userText) {
    try {
        const response = await fetch('http://127.0.0.1', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userText }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        // The bot's response comes from the Python server
        appendMessage(data.response, 'bot-message');

    } catch (error) {
        console.error("Error connecting to the Python server:", error);
        appendMessage("Error: Could not reach the bot server (Is Python running?). Try running 'python Pythone.py' in your terminal.", 'bot-message');
    }
}


function appendMessage(text, type) {
    const messageDiv = document.createElement('div');
    // The Python code sends markdown bolding (**) which we should handle in JS for better display
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>'); 
    messageDiv.classList.add('message', type);
    messageDiv.innerHTML = text; // Use innerHTML to render the <strong> tags
    chatWindow.appendChild(messageDiv);
    // Scroll to the bottom
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

// ... (Keep all your Timer Functions: updateTimerDisplay, startTimer, pauseTimer, resetTimer, etc. as they were) ...

// Initialize display on load
updateTimerDisplay();

// Optional: Allow pressing Enter to send message
userInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});
