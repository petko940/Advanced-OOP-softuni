def accommodate(*args, **kwargs):
    rooms_sorted = {}
    for number, capacity in sorted(kwargs.items(), key=lambda x: (x[1], x[0])):
        number = int(number.split("_")[1])
        rooms_sorted[number] = capacity

    rooms_sorted_length = len(rooms_sorted)
    taken_rooms = {}
    total_accommodations = 0
    total_number_of_unaccommodated_guests = 0
    for guest in args:
        for room_number, cap in rooms_sorted.items():
            if cap >= guest:
                total_accommodations += 1
                rooms_sorted.pop(room_number)
                taken_rooms[room_number] = guest
                break
        else:
            total_number_of_unaccommodated_guests += guest

    taken_rooms_length = len(taken_rooms)
    output = []
    if taken_rooms:
        output.append(f"A total of {total_accommodations} accommodations were completed!")
        for room_number, guest in sorted(taken_rooms.items(), key=lambda x: x[0]):
            output.append(f"<Room {room_number} accommodates {guest} guests>")
    else:
        output.append(f"No accommodations were completed!")

    if total_number_of_unaccommodated_guests:
        output.append(f"Guests with no accommodation: {total_number_of_unaccommodated_guests}")

    if rooms_sorted_length - taken_rooms_length:
        output.append(f"Empty rooms: {rooms_sorted_length - taken_rooms_length}")

    return "\n".join(output)
