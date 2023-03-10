from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @staticmethod
    def from_stars(stars_count: int):
        return Hotel(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for x in self.rooms:
            if x.number == room_number:
                x.take_room(people)

    def free_room(self, room_number):
        for x in self.rooms:
            if x.number == room_number:
                x.free_room()

    def status(self):
        guests, free_rooms, taken_rooms = 0, [], []
        for room in self.rooms:
            if room.is_taken:
                taken_rooms.append(room.number)
                guests += room.guests
                # self.guests += room.guests
            else:
                free_rooms.append(room.number)

        output = [f"Hotel {self.name} has {guests} total guests",
                  f"Free rooms: {', '.join(str(x) for x in free_rooms)}",
                  f"Taken rooms: {', '.join(str(x) for x in taken_rooms)}"]

        # output = [f"Hotel {self.name} has {self.guests} total guests",
        #           f"Free rooms: {', '.join(str(x) for x in free_rooms)}",
        #           f"Taken rooms: {', '.join(str(x) for x in taken_rooms)}"]

        return "\n".join(output)

