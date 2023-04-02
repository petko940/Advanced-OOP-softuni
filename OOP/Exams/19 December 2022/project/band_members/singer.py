from project.band_members.musician import Musician


class Singer(Musician):
    @property
    def type_of_musician(self):
        return {"sing high pitch notes",
                "sing low pitch notes"}
