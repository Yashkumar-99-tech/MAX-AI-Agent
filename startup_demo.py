from plugins.base_plugin import BasePlugin


class DemoPlugin(BasePlugin):

    def __init__(self):
        super().__init__()
        self.name = "Demo Plugin"

    def can_handle(self, command):
        return True

    def execute(self, command):
        return "✅ Plugin Working Successfully"


plugin = DemoPlugin()

if __name__ == '__main__':
    print(plugin.execute("hello"))
