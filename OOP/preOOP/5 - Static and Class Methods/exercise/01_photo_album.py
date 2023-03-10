from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for x in range(len(self.photos)):
            if len(self.photos[x]) < 4:
                self.photos[x].append(label)

                return f"{label} photo added successfully on page {x + 1} slot {len(self.photos[x])}"
        return "No more free slots"

    def display(self):
        output = "-----------\n"
        for x in range(self.pages):
            for y in self.photos[x]:
                if y == self.photos[x][-1]:
                    output += f"[]"
                elif y != " ":
                    output += "[] "

            output += "\n"
            output += "-----------\n"
        return output


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
