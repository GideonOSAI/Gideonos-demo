import os
import json
from playsound import playsound
from voice import say
from wakeword import listen_for_wakeword
from listen import recognize_speech
from gideon_brain import respond_to_query

def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_memory(memory):
    with open("memory.json", "w") as f:
        json.dump(memory, f, indent=2)

def parse_remember_command(command):
    if " is " in command:
        key, value = command.split(" is ", 1)
        return key.strip(), value.strip()
    return command.strip(), "remembered"

def list_memories(memory):
    if not memory:
        say("I don't have any memories stored yet.")
    else:
        say("Here are the things I remember:")
        for key, value in memory.items():
            say(f"{key} is {value}")

def delete_memory(memory, key):
    if key in memory:
        del memory[key]
        save_memory(memory)
        say(f"I've deleted the memory for '{key}'.")
    else:
        say(f"I don't have any memory of '{key}'.")

def main():
    memory = load_memory()
    say("Gideon system online.")

    while True:
        print("Listening for wake word...")
        if listen_for_wakeword():
            say("What can I do for you?")
            try:
                user_input = recognize_speech()
            except Exception as e:
                say("Sorry, I didn't catch that.")
                continue

            if user_input:
                user_input_lower = user_input.lower()
                print(f"User said: {user_input}")

                if user_input_lower in ["exit", "quit", "shutdown"]:
                    say("Shutting down. Goodbye.")
                    break

                if user_input_lower.startswith("remember"):
                    content = user_input[8:].strip()
                    key, value = parse_remember_command(content)
                    memory[key] = value
                    save_memory(memory)
                    say(f"I've saved '{key}' as '{value}' in my database.")
                elif user_input_lower.startswith("recall") or user_input_lower.startswith("what do you remember about"):
                    if user_input_lower.startswith("recall"):
                        key = user_input_lower[6:].strip()
                    else:
                        key = user_input_lower.replace("what do you remember about", "").strip()
                    value = memory.get(key)
                    if value:
                        say(f"I remember: {key} is {value}.")
                    else:
                        say(f"I don't have any memory of '{key}'.")
                elif user_input_lower.startswith("list memories") or user_input_lower == "what do you remember":
                    list_memories(memory)
                elif user_input_lower.startswith("delete memory") or user_input_lower.startswith("forget"):
                    if user_input_lower.startswith("delete memory"):
                        key = user_input_lower[13:].strip()
                    else:
                        key = user_input_lower[6:].strip()
                    delete_memory(memory, key)
                else:
                    try:
                        response = respond_to_query(user_input, memory)
                        say(response)
                    except Exception as e:
                        say("Sorry, I couldn't process your request.")

if __name__ == "__main__":
    main()