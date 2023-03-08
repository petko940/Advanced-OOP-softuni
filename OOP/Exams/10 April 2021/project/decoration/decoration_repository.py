class DecorationRepository:
    def __init__(self):
        self.decorations: list = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        for x in self.decorations:
            if x.__class__.__name__ == decoration_type:
                return x
        return "None"
