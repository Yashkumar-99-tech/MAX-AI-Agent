import os


def execute(command):

    command = command.lower()

    if "downloads" in command:

        os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))

        return "Opening Downloads."

    elif "documents" in command:

        os.startfile(os.path.join(os.path.expanduser("~"), "Documents"))

        return "Opening Documents."

    elif "desktop" in command:

        os.startfile(os.path.join(os.path.expanduser("~"), "Desktop"))

        return "Opening Desktop."

    return None