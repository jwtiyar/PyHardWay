class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, description):
        return self.paths.get(direction, None)

    def add_path(self, paths):
        self.paths.update(paths)