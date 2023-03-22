from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: list[Band] = []
        self.musicians: list[Musician] = []
        self.concerts: list[Concert] = []

    @property
    def valid_musician_types(self):
        return {"Guitarist": Guitarist,
                "Drummer": Drummer,
                "Singer": Singer}

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.valid_musician_types:
            raise ValueError("Invalid musician type!")

        musician = [m for m in self.musicians if m.name == name]
        if musician:
            raise Exception(f"{name} is already a musician!")

        new_musician = self.valid_musician_types[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = [b for b in self.bands if b.name == name]
        if band:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = [c for c in self.concerts if c.place == place]
        if concert:
            raise Exception(f"{place} is already registered for {genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = [m for m in self.musicians if m.name == musician_name]
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician[0])
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        members = [m.name for m in band.members]
        if musician_name not in members:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        musician = [x for x in band.members if x.name == musician_name][0]
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    @property
    def singer_types(self):
        return ["sing high pitch notes",
                "sing low pitch notes"]

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]

        singers = [s for s in band.members if s.__class__.__name__ == "Singer"]
        drummers = [s for s in band.members if s.__class__.__name__ == "Drummer"]
        guitarists = [s for s in band.members if s.__class__.__name__ == "Guitarist"]
        if not singers or not drummers or not guitarists:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = [c for c in self.concerts if c.place == concert_place][0]
        fail = False
        singer_type, drummer_types, guitarist_type = [], [], []
        for s in singers:
            singer_type.extend(s.skills)
        for d in drummers:
            drummer_types.extend(d.skills)
        for g in guitarists:
            guitarist_type.extend(g.skills)

        if concert.genre == "Rock":
            if "play the drums with drumsticks" not in drummer_types:
                fail = True
            if "sing high pitch notes" not in singer_type:
                fail = True
            if "play rock" not in guitarist_type:
                fail = True

        elif concert.genre == "Metal":
            if "play the drums with drumsticks" not in drummer_types:
                fail = True
            if "sing low pitch notes" not in singer_type:
                fail = True
            if "play metal" not in guitarist_type:
                fail = True

        elif concert.genre == "Jazz":
            if "play the drums with drum brushes" not in drummer_types:
                fail = True
            a = ["sing high pitch notes", "sing low pitch notes"]
            if a[0] not in singer_type:
                fail = True
            if a[1] not in singer_type:
                fail = True
            if "play jazz" not in guitarist_type:
                fail = True

        if fail:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
