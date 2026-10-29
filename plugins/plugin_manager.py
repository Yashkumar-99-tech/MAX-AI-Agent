import os
import importlib

from plugins.base_plugin import BasePlugin


class PluginManager:

    def __init__(self):

        self.plugins = []

    def load_plugins(self):

        plugin_folder = os.path.dirname(__file__)

        for file in os.listdir(plugin_folder):

            if (
                file.endswith("_plugin.py")
                and file != "base_plugin.py"
            ):

                module_name = file[:-3]

                module = importlib.import_module(
                    f"plugins.{module_name}"
                )

                for item in dir(module):

                    obj = getattr(module, item)

                    if (
                        isinstance(obj, type)
                        and issubclass(obj, BasePlugin)
                        and obj != BasePlugin
                    ):

                        self.plugins.append(obj())

                        print(f"✅ Loaded : {obj.__name__}")

    def execute(self, command):

        for plugin in self.plugins:

            if plugin.can_handle(command):

                return plugin.execute(command)

        return None


plugin_manager = PluginManager()