from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    @property
    def valid_musician_types(self):
        return {"Guitarist": Guitarist,
                "Drummer": Drummer,
                "Singer": Singer}

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.valid_musician_types:
            raise ValueError("Invalid musician type!")

        try:
            next(x for x in self.musicians if x.name == name)
        except StopIteration:
            new_musician = self.valid_musician_types[musician_type](name, age)
            self.musicians.append(new_musician)
            return f"{name} is now a {musician_type}."

        raise Exception(f"{name} is already a musician!")

    def create_band(self, name: str):
        try:
            next(x for x in self.bands if x.name == name)
        except StopIteration:
            new_band = Band(name)
            self.bands.append(new_band)
            return f"{name} was created."

        raise Exception(f"{name} band is already created!")

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        try:
            concert = next(x for x in self.concerts if x.place == place)
            raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")

        except StopIteration:
            new_concert = Concert(genre, audience, ticket_price, expenses, place)
            self.concerts.append(new_concert)
            return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = [x for x in self.musicians if x.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = next(x for x in self.bands if x.name == band_name)
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = next(x for x in self.bands if x.name == band_name)
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        for x in band.members:
            if x.name == musician_name:
                musician = x
                break
        else:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        members = set([x.__class__.__name__ for x in self.musicians])
        if len(members) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = next(x for x in self.concerts if x.place == concert_place)
        band = [x for x in self.bands if x.name == band_name][0]

        drummers = [x for x in band.members if x.__class__.__name__ == "Drummer"]
        singer = [x for x in band.members if x.__class__.__name__ == "Singer"]
        guitarist = [x for x in band.members if x.__class__.__name__ == "Guitarist"]

        drummer_type = []
        for d in drummers:
            drummer_type.extend(d.skills)
        singer_type = []
        for s in singer:
            singer_type.extend(s.skills)
        guitarist_type = []
        for g in guitarist:
            guitarist_type.extend(g.skills)

        fail = False
        if concert.genre == 'Rock':
            if "play the drums with drumsticks" not in drummer_type \
                    or "sing high pitch notes" not in singer_type \
                    or 'play rock' not in guitarist_type:
                fail = True
        elif concert.genre == "Metal":
            if 'play the drums with drumsticks' not in drummer_type \
                    or "sing low pitch notes" not in singer_type \
                    or 'play metal' not in guitarist_type:
                fail = True
        elif concert.genre == 'Jazz':
            if "play the drums with drum brushes" not in drummer_type \
                    or "sing high pitch notes" not in singer_type \
                    or "sing low pitch notes" not in singer_type \
                    or 'play jazz' not in guitarist_type:
                fail = True

        if fail:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
