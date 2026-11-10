
import speech_recognition as sr
import pyttsx3
from brain import think
from actions import perform_action
from memory import remember, search_memory, get_memory

# ==============================
# JARVIS VOICE ENGINE
# ==============================

engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def speak(text):
    text = str(text)
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()


# ==============================
# MICROPHONE
# ==============================

recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("\nJARVIS: Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("YOU:", command)
        return command

    except sr.UnknownValueError:
        speak("Sorry Sir, I could not understand you.")
        return ""

    except sr.RequestError:
        speak("Sorry Sir, the speech recognition service is unavailable.")
        return ""


# ==============================
# SHOW MEMORY
# ==============================

def show_memory():
    memories = get_memory()

    if not memories:
        speak("I don't have any memories yet, Sir.")
        return

    recent_memories = memories[-5:]

    action_names = {
        "OPEN_CHROME": "opened Chrome",
        "OPEN_VSCODE": "opened VS Code",
        "OPEN_NOTEPAD": "opened Notepad",
        "OPEN_CALCULATOR": "opened Calculator",
        "GOOGLE_SEARCH": "searched Google",
        "YOUTUBE_SEARCH": "searched YouTube",
        "TIME": "checked the time",
        "VOLUME_UP": "increased the volume",
        "VOLUME_DOWN": "decreased the volume",
        "VOLUME_MUTE": "muted the volume",
        "VOLUME_UNMUTE": "unmuted the volume",
        "VOLUME_SET": "changed the volume",
        "BRIGHTNESS_UP": "increased the brightness",
        "BRIGHTNESS_DOWN": "decreased the brightness",
        "BRIGHTNESS_SET": "changed the brightness",
        "BRIGHTNESS_MAX": "set the brightness to maximum",
    }

    speak("Here are your five most recent memories, Sir.")

    for item in recent_memories:
        user_text = item.get("user", "")
        response = item.get("jarvis", "")
        response_text = action_names.get(response, response)

        speak(f"You said {user_text}.")
        speak(f"My response was {response_text}.")


# ==============================
# MAIN JARVIS
# ==============================

speak("Hello Sir. JARVIS is online.")

while True:
    command = listen()

    if not command:
        continue

    action = think(command)

    # Save useful commands in memory
    if action not in ["SEARCH_MEMORY", "SHOW_MEMORY", "EXIT"]:
        if action == "YOUTUBE_SEARCH":
            search_text = command.lower()

            words_to_remove = [
                "jarvis", "please", "search",
                "youtube", "yt", "for", "on"
            ]

            clean_words = [
                word for word in search_text.split()
                if word not in words_to_remove
            ]

            remember(" ".join(clean_words).strip(), action)
        else:
            remember(command, action)

    # Exit
    if action == "EXIT":
        speak("Goodbye Sir.")
        break

    # Open applications
    elif action == "OPEN_CHROME":
        perform_action(action)
        speak("Chrome is open, Sir.")

    elif action == "OPEN_VSCODE":
        perform_action(action)
        speak("VS Code is open, Sir.")

    elif action == "OPEN_NOTEPAD":
        perform_action(action)
        speak("Notepad is open, Sir.")

    elif action == "OPEN_CALCULATOR":
        perform_action(action)
        speak("Calculator is open, Sir.")

    # Search memory
    elif action == "SEARCH_MEMORY":
        results = search_memory("")
        search_results = [
            item for item in results
            if item["jarvis"] in ["YOUTUBE_SEARCH", "GOOGLE_SEARCH"]
        ]

        if search_results:
            last_memory = search_results[-1]
            speak(
                f"Your previous search was {last_memory['user']}, Sir."
            )
        else:
            speak("I could not find any previous search, Sir.")

    # Show memory
    elif action == "SHOW_MEMORY":
        show_memory()

    # Volume control
    elif action.startswith("VOLUME_"):
        response = perform_action(action, command)
        speak(response)

    # Brightness control
    elif action.startswith("BRIGHTNESS_"):
        response = perform_action(action, command)
        speak(response)

    # Google search
    elif action == "GOOGLE_SEARCH":
        perform_action(action, command)
        speak("Searching Google, Sir.")

    # YouTube search
    elif action == "YOUTUBE_SEARCH":
        perform_action(action, command)
        speak("Searching YouTube, Sir.")

    # Time
    elif action == "TIME":
        current_time = perform_action(action)
        speak(f"The current time is {current_time}, Sir.")

    # Normal responses
    else:
        speak(action)
