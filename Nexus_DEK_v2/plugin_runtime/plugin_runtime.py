class PluginRuntime:
    def __init__(self):
        self.plugins = {}

    def register(self, name, fn):
        self.plugins[name] = fn

    def execute(self, name, payload):
        if name not in self.plugins:
            raise Exception("Plugin not found")
        return self.plugins[name](payload)
