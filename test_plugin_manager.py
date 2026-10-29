from plugins.plugin_manager import plugin_manager

plugin_manager.load_plugins()

print()

print(plugin_manager.execute("hello"))

print(plugin_manager.execute("youtube"))