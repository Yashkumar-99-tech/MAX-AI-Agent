import webbrowser


def execute(command):

    command = command.lower()

    if "youtube" in command:

        webbrowser.open("https://www.youtube.com")

        return "Opening YouTube."

    elif "google" in command:

        webbrowser.open("https://www.google.com")

        return "Opening Google."

    elif "chatgpt" in command:

        webbrowser.open("https://chat.openai.com")

        return "Opening ChatGPT."

    return None