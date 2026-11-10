import subprocess
from pycaw.pycaw import AudioUtilities
from datetime import datetime
import webbrowser
import wmi

def open_chrome():
    print("JARVIS: Opening Chrome...")
    subprocess.Popen(
        ["cmd", "/c", "start", "", "chrome"],
        shell=True
    )


def open_vscode():
    print("JARVIS: Opening VS Code...")
    subprocess.Popen(
        ["cmd", "/c", "start", "", "code"],
        shell=True
    )


def open_notepad():
    print("JARVIS: Opening Notepad...")
    subprocess.Popen(
        ["notepad.exe"]
    )


def open_calculator():
    print("JARVIS: Opening Calculator...")
    subprocess.Popen(
        ["calc.exe"]
    )


def get_time():
    current_time = datetime.now().strftime("%I:%M %p")
    print("JARVIS: The current time is", current_time)
    return current_time

def google_search(command):
    search_query = command.replace("search", "").replace("google", "").strip()

    if search_query == "":
        print("JARVIS: What should I search for?")
        return

    url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
    webbrowser.open(url)

    print("JARVIS: Searching Google for", search_query)

def youtube_search(command):

    words_to_remove = [
        "jarvis",
        "please",
        "search",
        "youtube",
        "yt",
        "for",
        "on"
    ]

    words = command.lower().split()

    clean_words = []

    for word in words:
        if word not in words_to_remove:
            clean_words.append(word)

    search_query = " ".join(clean_words).strip()

    if search_query == "":
        print("JARVIS: What should I search for on YouTube?")
        return

    url = "https://www.youtube.com/results?search_query=" + search_query.replace(" ", "+")
    webbrowser.open(url)

    print("JARVIS: Searching YouTube for", search_query)

def control_volume(action, command=None):
    try:
        device = AudioUtilities.GetSpeakers()
        current_volume = device.volume_percent

        if action == "VOLUME_UP":
            device.volume_percent = min(100, current_volume + 10)
            return f"Volume increased to {device.volume_percent:.0f} percent, Sir."

        elif action == "VOLUME_DOWN":
            device.volume_percent = max(0, current_volume - 10)
            return f"Volume decreased to {device.volume_percent:.0f} percent, Sir."

        elif action == "VOLUME_MUTE":
            device.EndpointVolume.SetMute(1, None)
            return "Volume muted, Sir."

        elif action == "VOLUME_UNMUTE":
            device.EndpointVolume.SetMute(0, None)
            return "Volume unmuted, Sir."

        elif action == "VOLUME_SET":
            import re

            match = re.search(r"\b(\d{1,3})\b", command or "")

            if not match:
                return "Please say a volume percentage from 0 to 100, Sir."

            percentage = int(match.group(1))
            percentage = max(0, min(100, percentage))
            device.volume_percent = percentage

            return f"Volume set to {percentage} percent, Sir."

    except Exception as error:
        print("Volume control error:", error)
        return "Sorry Sir, I could not control the volume."

    return "Sorry Sir, I could not control the volume."


def control_brightness(action, command=None):
    try:
        monitor = wmi.WMI(namespace="wmi")
        brightness_info = monitor.WmiMonitorBrightness()

        if not brightness_info:
            return "Sorry Sir, brightness control is unavailable."

        current = brightness_info[0].CurrentBrightness

        if action == "BRIGHTNESS_UP":
            target = min(100, current + 10)

        elif action == "BRIGHTNESS_DOWN":
            target = max(0, current - 10)

        elif action == "BRIGHTNESS_MAX":
            target = 100

        elif action == "BRIGHTNESS_SET":
            import re
            match = re.search(r"\b(\d{1,3})\b", command or "")

            if not match:
                return "Please say a brightness percentage, Sir."

            target = max(0, min(100, int(match.group(1))))

        else:
            return "Sorry Sir, I don't know that brightness command."

        for item in monitor.WmiMonitorBrightnessMethods():
            item.WmiSetBrightness(target, 0)

        return f"Brightness set to {target} percent, Sir."

    except Exception as error:
        print("Brightness control error:", error)
        return "Sorry Sir, I could not change the brightness."


def perform_action(action, command=None):

    
    if action.startswith("VOLUME_"):
        return control_volume(action, command)
    
    
    elif action.startswith("BRIGHTNESS_"):
        return control_brightness(action, command)

    elif action == "OPEN_CHROME":
        open_chrome()


    if action == "OPEN_CHROME":
        open_chrome()

    elif action == "OPEN_VSCODE":
        open_vscode()

    elif action == "OPEN_NOTEPAD":
        open_notepad()

    elif action == "OPEN_CALCULATOR":
        open_calculator()

    elif action == "TIME":
        return get_time()

    elif action == "GOOGLE_SEARCH":
        google_search(command)

    elif action == "YOUTUBE_SEARCH":
        youtube_search(command)

    else:
        print("JARVIS: I don't know this action yet.")