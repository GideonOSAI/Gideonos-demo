import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

from physics_engine import answer_physics_question

MEMORY_FILE = Path("memory.json")

def load_memory() -> Dict[str, Any]:
    """Load memory from the JSON file."""
    if MEMORY_FILE.exists():
        try:
            with MEMORY_FILE.open("r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

def save_memory(memory: Dict[str, Any]) -> None:
    """Save memory to the JSON file."""
    try:
        with MEMORY_FILE.open("w", encoding="utf-8") as f:
            json.dump(memory, f, indent=2)
    except IOError:
        pass  # Optionally log the error

def add_fact_to_memory(memory: Dict[str, Any], fact: str) -> None:
    """Add a fact to memory with a timestamp."""
    timestamp = datetime.now().isoformat()
    memory[fact] = {"status": "remembered", "timestamp": timestamp}
    save_memory(memory)

def get_memory_facts(memory: Dict[str, Any]) -> str:
    """Return a string listing all remembered facts."""
    if memory:
        facts = [f"{fact} (added on {info['timestamp']})" for fact, info in memory.items()]
        return "I remember: " + "; ".join(facts)
    return "I don't remember anything yet."

def get_current_time() -> str:
    """Return the current time as a formatted string."""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def process_input(user_input: str, memory: Dict[str, Any]) -> str:
    """Process user input and return a response."""
    normalized = user_input.strip().lower()

    if normalized.startswith("remember"):
        fact = normalized.replace("remember", "", 1).strip()
        if fact:
            add_fact_to_memory(memory, fact)
            return f"I have saved: {fact}"
        return "Please tell me what to remember."

    if normalized.startswith("what do you remember"):
        return get_memory_facts(memory)

    physics_keywords = {"gravity", "light", "force", "law", "acceleration", "physics"}
    if any(word in normalized for word in physics_keywords):
        return answer_physics_question(user_input)

    if "how are you" in normalized:
        return "I'm functioning within optimal parameters."

    if "clear memory" in normalized:
        memory.clear()
        save_memory(memory)
        return "Memory cleared."

    if "time" in normalized:
        return f"The current time is {get_current_time()}."

    return "I'm not sure how to respond to that yet."

def respond_to_query(query: str) -> str:
    """Respond to common queries."""
    normalized = query.strip().lower()

    if "who are you" in normalized:
        return "I am Gideon, your AI assistant."
    if "what is force" in normalized:
        return "Force equals mass times acceleration, according to Newton's second law."
    if "what is velocity" in normalized:
        return "Velocity is the speed of something in a given direction."
    if "what is energy" in normalized:
        return "Energy is the capacity to do work. It comes in many forms like kinetic, thermal, or potential energy."
    if any(greet in normalized for greet in ("hello", "hi")):
        return "Hello there! How can I help you today?"
    if "bye" in normalized:
        return "Goodbye. I'm always here if you need me."
    if "time" in normalized:
        return f"The current time is {get_current_time()}."
    return "I'm not sure how to answer that yet, but I'm learning more every day."

# Usage example:
if __name__ == "__main__":
    memory = load_memory()
    # Example: print(process_input("remember the sky is blue", memory))