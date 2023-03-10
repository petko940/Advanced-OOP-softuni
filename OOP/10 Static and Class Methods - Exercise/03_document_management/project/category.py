class Category:
    def __init__(self, id_num: int, name: str):
        self.id = id_num
        self.name = name

    def edit(self, new_name: str):
        self.name = new_name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"
