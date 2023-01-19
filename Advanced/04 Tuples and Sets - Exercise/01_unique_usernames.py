class Usernames:
    def __init__(self, names_number):
        self.names_number = names_number
        self.unique_name = set()

    def fill_unique_name(self):
        for _ in range(self.names_number):
            name = input()
            self.unique_name.add(name)

    def __repr__(self):
        [print(x) for x in self.unique_name]


users = Usernames(int(input()))
users.fill_unique_name()
users.__repr__()
