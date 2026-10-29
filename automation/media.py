import pyautogui


def execute(command):

    command = command.lower()

    if "pause" in command:

        pyautogui.press("playpause")

        return "Media Paused."

    elif "play music" in command:

        pyautogui.press("playpause")

        return "Playing Music."

    elif "next song" in command:

        pyautogui.press("nexttrack")

        return "Next Song."

    elif "previous song" in command:

        pyautogui.press("prevtrack")

        return "Previous Song."

    elif "volume up" in command:

        pyautogui.press("volumeup")

        return "Increasing Volume."

    elif "volume down" in command:

        pyautogui.press("volumedown")

        return "Decreasing Volume."

    elif "mute" in command:

        pyautogui.press("volumemute")

        return "Muted."

    return None