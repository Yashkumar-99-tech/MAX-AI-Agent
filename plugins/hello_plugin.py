from plugins.base_plugin import BasePlugin


class HelloPlugin(BasePlugin):

    def __init__(self):

        self.name = "Hello Plugin"

    def can_handle(self, command):

        return command.lower() == "hello"

    def execute(self, command):

        return "👋 Hello Yash! Plugin System Working."