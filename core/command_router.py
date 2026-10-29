from plugins.plugin_manager import plugin_manager
from ai.brain import ask_ai
from memory.context_manager import context

from automation import system
from automation import media
from automation import browser


class CommandRouter:

    def __init__(self):
        plugin_manager.load_plugins()

    def execute(self, command):

        context.add_user(command)

        # SYSTEM
        result = system.execute(command)
        if result:
            context.add_ai(result)
            return result

        # BROWSER
        result = browser.execute(command)
        if result:
            context.add_ai(result)
            return result

        # MEDIA
        result = media.execute(command)
        if result:
            context.add_ai(result)
            return result

        # PLUGINS
        result = plugin_manager.execute(command)
        if result:
            context.add_ai(result)
            return result

        # AI
        reply = ask_ai(command)

        context.add_ai(reply)

        return reply


router = CommandRouter()