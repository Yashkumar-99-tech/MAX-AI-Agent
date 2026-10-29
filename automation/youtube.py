import pywhatkit
import webbrowser
import urllib.parse


def execute(command):

    command = command.lower().strip()

    if command.startswith("play "):

        song = command.replace("play", "", 1).strip()

        try:
            pywhatkit.playonyt(song)
            return f"Playing {song} on YouTube."
        except Exception:
            # Fallback: open YouTube search in the default browser
            query = urllib.parse.quote(song)
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)
            return f"Opened YouTube search for {song} in browser."

    return None