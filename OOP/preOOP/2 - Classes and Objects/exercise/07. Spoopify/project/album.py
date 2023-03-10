from project.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = [x for x in songs]

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return f"Cannot add songs. Album is published."

        if song.name in [x.name for x in self.songs]:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."
        for x in self.songs:
            if x.name == song_name:
                self.songs.remove(x)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        output = [f"Album {self.name}"]
        for x in self.songs:
            output.append(f"== {x.get_info()}")
        return '\n'.join(output)




