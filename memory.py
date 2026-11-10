
# ==========================================
#              JARVIS MEMORY
# ==========================================

import json
import os

MEMORY_FILE = "memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


conversation_memory = load_memory()


def remember(user_command, jarvis_response):
    if jarvis_response in ["SEARCH_MEMORY", "SHOW_MEMORY", "EXIT"]:
        return

    memory = {
        "user": user_command,
        "jarvis": jarvis_response
    }

    conversation_memory.append(memory)

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(conversation_memory, file, indent=4)


def get_memory():
    return conversation_memory


def search_memory(keyword):
    keyword = keyword.lower()

    results = []

    for memory in conversation_memory:
        if keyword in memory["user"].lower():
            results.append(memory)

    return results
