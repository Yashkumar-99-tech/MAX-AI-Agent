import pyautogui
import datetime


def execute(command):

    command = command.lower()

    if "screenshot" in command:

        filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"

        pyautogui.screenshot(filename)

        return f"Screenshot saved as {filename}"

    return None