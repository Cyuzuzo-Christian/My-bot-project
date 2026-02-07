"""
Project: Study Optimizer Bot (Student Wellness Initiative)
Author: Cyuzuzo Shami Set Christian
Date: January 10, 2026
Version: 1.0.0

Description:
This Python script powers a simple, rule-based chatbot designed to help students manage
their study habits using techniques like the Pomodoro method. It tracks focus sessions
and provides motivational tips to improve academic efficiency and mental wellness.

Interests in Computer Science & AI:
My journey into CS began with a passion for solving real-world problems through logic and automation.
I am particularly fascinated by Natural Language Processing (NLP) and how conversational AI can be
used ethically to improve daily life and education. This project is a practical application of
data structuring and user experience (UX) design, an area I am eager to explore further at the
university level.
"""

import time
import json

# --- 1. KNOWLEDGE BASE (General Study Tips) ---
STUDY_DB = {
    "tips": [
        {"title": "Pomodoro Technique", "summary": "Study for 25 minutes, then take a 5-minute break."},
        {"title": "Spaced Repetition", "summary": "Review material at increasing intervals over time to improve memory."},
        {"title": "Active Recall", "summary": "Force yourself to remember information from scratch instead of reviewing notes."},
        {"title": "Sleep Hygiene", "summary": "Aim for 7-9 hours of consistent sleep; it's crucial for memory consolidation."},
        {"title": "Manage Environment", "summary": "Find a quiet, distraction-free space to maximize focus."},
    ],
    "quotes": [
        "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is the sum of small efforts, repeated day in and day out. - Robert Collier",
    ]
}

# --- 2. USER SESSION STORAGE (Tracking progress) ---
user_session = {
    "name": "Student",
    "focus_sessions_completed_today": 0,
    "last_tip_index": -1
}

# --- 3. CORE BOT LOGIC FUNCTIONS ---

def get_tip():
    """Cycles through study tips."""
    user_session['last_tip_index'] = (user_session['last_tip_index'] + 1) % len(STUDY_DB['tips'])
    tip = STUDY_DB['tips'][user_session['last_tip_index']]
    return f"💡 **{tip['title']}**: {tip['summary']}"

def run_pomodoro():
    """Simulates a Pomodoro session. This would be a real timer in a UI application."""
    study_duration = 25 # minutes
    break_duration = 5  # minutes
    
    # In a command line bot, we simulate the time passing:
    print(f"🧠 Advisor Bot: Starting {study_duration}-minute focus session. Stay focused! (Simulated time passing...)")
    # time.sleep(study_duration * 60)
    print(f"🎉 Advisor Bot: Session complete! Time for a {break_duration}-minute break.")
    
    user_session['focus_sessions_completed_today'] += 1
    count = user_session['focus_sessions_completed_today']
    return f"You've completed {count} focus session{'s' if count > 1 else ''} today!"

def get_status():
    """Provides personalized status update."""
    count = user_session['focus_sessions_completed_today']
    if count == 0:
        return "You haven't completed any focus sessions today. Let's start one!"
    else:
        return f"You've completed {count} focus sessions today. Keep the momentum going!"

def handle_input(user_input):
    """Maps user input to the correct function (Simulated NLU)."""
    user_input = user_input.lower()

    # Custom Identity Responses
    if "who created you" in user_input or "who is your creator" in user_input or "who made you" in user_input:
        creator_name = "Cyuzuzo Shami Set Christian" 
        return f"I was designed and coded by the talented {creator_name} as part of a project to help students achieve academic excellence!"
    
    if "who are you" in user_input or "what are you" in user_input:
        return "I am the Study Optimizer Bot, your personal assistant for time management, focus, and study habit optimization."

    if "hello" in user_input or "hi" in user_input:
        return f"Hello {user_session['name']}! I'm your Study Optimizer Bot. Type 'help' to see how I can assist you."
    elif "help" in user_input:
        return "You can say: 'give me a tip', 'start session', or 'check status'."
    elif "give me a tip" in user_input or "tip" in user_input:
        return get_tip()
    elif "start session" in user_input or "pomodoro" in user_input:
        return run_pomodoro() 
    elif "check status" in user_input or "status" in user_input:
        return get_status()
    else:
        return "I am a simple bot. I didn't understand that. Try asking for 'help'."

# --- 4. INTERFACE LOOP (Command Line) ---

if __name__ == "__main__":
    print("Advisor Bot: Hi there! Type 'hello' to begin, or 'exit' to quit.")
    while True:
        user_input = input(f"{user_session['name']}> ")
        if user_input.lower() == 'exit':
            break
        response = handle_input(user_input)
        print(f"Advisor Bot: {response}")



