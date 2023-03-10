from project.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for x in self.albums:
            if x.name == album_name and x.published:
                return "Album has been published. It cannot be removed."
            if x.name == album_name and not x.published:
                self.albums.remove(x)
                return f"Album {album_name} has been removed."

        if album_name not in [x.name for x in self.albums]:
            return f"Album {album_name} is not found."

    def details(self):
        output = [f"Band {self.name}"]
        for x in self.albums:
            output.append(x.details())
        return '\n'.join(output)


