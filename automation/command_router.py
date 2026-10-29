from plugins.plugin_manager import plugin_manager
from ai.brain import ask_ai
from memory.context_manager import context

from automation import system
from automation import browser
from automation import youtube
from automation import media


class CommandRouter:

    def __init__(self):
        plugin_manager.load_plugins()

    def execute(self, command):

        context.add_user(command)

        print("\n========== ROUTER DEBUG ==========")
        print("Command :", command)

        # -----------------------------
        # SYSTEM
        # -----------------------------
        result = system.execute(command)

        print("System Result :", result)

        if result is not None:
            context.add_ai(result)
            return result

        # -----------------------------
        # BROWSER
        # -----------------------------
        result = browser.execute(command)

        print("Browser Result :", result)

        if result is not None:
            context.add_ai(result)
            return result

        # -----------------------------
        # YOUTUBE
        # -----------------------------
        result = youtube.execute(command)

        print("YouTube Result :", result)

        if result is not None:
            context.add_ai(result)
            return result

        # -----------------------------
        # MEDIA
        # -----------------------------
        result = media.execute(command)

        print("Media Result :", result)

        if result is not None:
            context.add_ai(result)
            return result

        # -----------------------------
        # PLUGINS
        # -----------------------------
        result = plugin_manager.execute(command)

        print("Plugin Result :", result)

        if result is not None:
            context.add_ai(result)
            return result

        # -----------------------------
        # AI
        # -----------------------------
        print("➡ Sending to Gemini...")

        reply = ask_ai(command)

        context.add_ai(reply)

        return reply


router = CommandRouter()