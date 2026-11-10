# ==========================================
#              JARVIS BRAIN
# ==========================================

def think(command):

    command = command.lower().strip()

    # Greetings
    if command in ["hello", "hi", "hey"]:
        return "Hello Sir. How can I help you?"

    # Identity
    elif "who are you" in command or "tum kon ho" in command:
        return "I am JARVIS, your personal AI assistant."

    # Chrome
    elif "chrome" in command:
        return "OPEN_CHROME"

    # Time
    elif "time" in command or "samay" in command:
        return "TIME"

    # Memory Search
    elif (
       "what did i search" in command
       or "what did i" in command
       or "previous search" in command
       or "my previous search" in command
    ):
       return "SEARCH_MEMORY"

    
    # Show Memory
    elif (
        "what do you remember" in command
        or "show my memory" in command
        or "what did i do" in command
    ):
        return "SHOW_MEMORY"

    
    # Volume: unmute before mute
    elif "unmute" in command or "sound on" in command:
        return "VOLUME_UNMUTE"

    elif "mute" in command or "silent volume" in command:
        return "VOLUME_MUTE"

    # Set a specific volume percentage
    elif "set volume" in command or "volume to" in command:
        return "VOLUME_SET"

    # Increase volume
    elif (
        "increase volume" in command
        or "volume up" in command
        or "turn up volume" in command
        or "louder" in command
        
        or "raise volume" in command
        or "increase the volume" in command

    ):
        return "VOLUME_UP"

    # Decrease volume
    elif (
        "decrease volume" in command
        or "volume down" in command
        or "turn down volume" in command
        or "lower volume" in command
    ):
        return "VOLUME_DOWN"

    
    # Brightness control
    elif "maximum brightness" in command or "max brightness" in command:
        return "BRIGHTNESS_MAX"

    elif "increase brightness" in command or "brightness up" in command:
        return "BRIGHTNESS_UP"

    elif "decrease brightness" in command or "brightness down" in command:
        return "BRIGHTNESS_DOWN"

    elif "set brightness" in command or "brightness to" in command:
        return "BRIGHTNESS_SET"

    # YouTube Search
    elif "youtube" in command or "yt" in command:
        return "YOUTUBE_SEARCH"
    
    # Google Search
    elif "search" in command or "google" in command:
        return "GOOGLE_SEARCH"
    
    # VS Code
    elif "vs code" in command or "vscode" in command or "visual studio code" in command:
        return "OPEN_VSCODE"

    # Notepad
    elif "notepad" in command:
        return "OPEN_NOTEPAD"

    # Calculator
    elif "calculator" in command or "calc" in command:
        return "OPEN_CALCULATOR"

    # Exit
    elif "exit" in command or "stop" in command or "bye" in command:
        return "EXIT"

    # Unknown
    else:
        return "Sorry Sir, I don't know how to do that yet."


if __name__ == "__main__":

    print("================================")
    print("        JARVIS BRAIN")
    print("================================")

    while True:

        command = input("YOU: ")

        result = think(command)

        print("JARVIS:", result)

        if result == "EXIT":
            break