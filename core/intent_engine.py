import re


class IntentEngine:

    def detect(self, command: str):

        text = command.lower().strip()

        # Play Music
        if text.startswith("play "):
            song = text.replace("play", "", 1).strip()

            return {
                "intent": "PLAY_MUSIC",
                "data": song
            }

        # Open Website
        if text.startswith("open "):
            app = text.replace("open", "", 1).strip()

            return {
                "intent": "OPEN_APP",
                "data": app
            }

        # Remember
        if text.startswith("remember "):
            memory = text.replace("remember", "", 1).strip()

            return {
                "intent": "REMEMBER",
                "data": memory
            }

        # Screenshot
        if "screenshot" in text:

            return {
                "intent": "SCREENSHOT",
                "data": None
            }

        return {
            "intent": "AI",
            "data": command
        }


intent_engine = IntentEngine()
