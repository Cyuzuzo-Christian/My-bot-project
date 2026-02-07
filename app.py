from flask import Flask, render_template, request, jsonify
import study_bot  # Import your chatbot logic module

app = Flask(__name__)

# Route to serve the main HTML file
@app.route('/')
def index():
    return render_template('index.html')

# API Endpoint to receive messages from the frontend and send responses
@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get("message")
    
    # Pass the user's message to the handle_input function in study_bot.py
    bot_response = study_bot.handle_input(user_message)
    
    # Return the bot's response as a JSON object that the JavaScript can read
    return jsonify({"response": bot_response})

# --- Server Start Command ---
# This ensures the server starts immediately when you run the file. 
app.run(debug=True, port=5000) 

