from project.band_members.musician import Musician


class Drummer(Musician):
    @property
    def type_of_musician(self):
        return {"play the drums with drumsticks",
                "play the drums with drum brushes",
                "read sheet music"}
