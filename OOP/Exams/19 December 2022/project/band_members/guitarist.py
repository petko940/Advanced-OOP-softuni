from project.band_members.musician import Musician


class Guitarist(Musician):
    @property
    def type_of_musician(self):
        return {"play jazz",
                "play rock",
                "play metal"}
