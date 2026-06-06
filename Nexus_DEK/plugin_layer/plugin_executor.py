class PluginExecutor:
    def __init__(self):
        self.registry = {}

    def register(self, name, fn):
        self.registry[name] = fn

    def execute(self, name, payload):
        if name not in self.registry:
            raise Exception("Plugin not found")
        return self.registry[name](payload)
