from math import ceil


class PhotoAlbum:
    PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PAGE))

    def add_photo(self, label: str):
        for i in range(self.pages):
            if len(self.photos[i]) < PhotoAlbum.PAGE:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"

        return "No more free slots"

    def display(self):
        output = ['-' * 11]
        for page in self.photos:
            output.append(("[] " * len(page)).strip())
            output.append('-' * 11)
        return '\n'.join(output)

