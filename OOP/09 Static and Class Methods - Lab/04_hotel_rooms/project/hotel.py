from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for r in self.rooms:
            if r.number == room_number:
                r.take_room(people)
                self.guests += r.guests

    def free_room(self, room_number):
        for r in self.rooms:
            if r.number == room_number:
                self.guests -= r.guests
                r.free_room()


    def status(self):
        free_rooms = [r for r in self.rooms if not r.is_taken]
        taken_rooms = [r for r in self.rooms if r.is_taken]

        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(str(x.number) for x in free_rooms)}\n" \
               f"Taken rooms: {', '.join(str(x.number) for x in taken_rooms)}"
