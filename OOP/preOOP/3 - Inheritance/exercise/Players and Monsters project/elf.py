from project.hero import Hero


class Elf(Hero):

    def __str__(self):
        return f"{self.username} of type {__class__.__name__} has level {self.level}"


hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)