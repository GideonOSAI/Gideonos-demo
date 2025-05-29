from playsound import playsound
from voice import say
from wakeword import listen_for_wakeword
from recognize import recognize_speech # type: ignore
from gideon_brain import respond_to_query
import json
import os
import re

def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_memory(memory):
    with open("memory.json", "w") as f:
        json.dump(memory, f, indent=2)

def parse_remember_command(text):
    # Example: "remember my birthday is June 1st"
    match = re.match(r".*remember (.+?) is (.+)", text, re.IGNORECASE)
    if match:
        key = match.group(1).strip()
        value = match.group(2).strip()
        return key, value
    # Fallback: "remember groceries"
    key = text.replace("remember", "").strip()
    return key, "remembered"

def parse_recall_command(text):
    # Example: "what did you remember about my birthday"
    match = re.match(r".*remember about (.+)", text, re.IGNORECASE)
    if match:
        key = match.group(1).strip()
        return key
    return None

def main():
    try:
        playsound(os.path.join(os.getcwd(), "startup_chime.mp3"))
    except Exception as e:
        print(f"Startup sound error: {e}")

    memory = load_memory()
    say("Gideon system online.")

    try:
        while True:
            if listen_for_wakeword():
                say("What can I do for you?")
                user_input = recognize_speech()

                if not user_input:
                    say("Sorry, I didn't catch that. Please repeat.")
                    continue

                print(f"Heard: {user_input}")

                if "remember" in user_input.lower():
                    key, value = parse_remember_command(user_input)
                    memory[key] = value
                    save_memory(memory)
                    say(f"I have saved '{key}' as '{value}' in my database.")
                elif "remember about" in user_input.lower():
                    key = parse_recall_command(user_input)
                    if key and key in memory:
                        say(f"I remember {key} is {memory[key]}.")
                    else:
                        say(f"I don't have anything remembered about {key}.")
                else:
                    response = respond_to_query(user_input)
                    say(response)
    except KeyboardInterrupt:
        say("Shutting down. Goodbye!")
        save_memory(memory)

if __name__ == "__main__":
    main()
