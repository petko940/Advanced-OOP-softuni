def accommodate_new_pets(*args):
    available_capacity = args[0]
    maximum_weight_limit = args[1]

    all_pets = True

    pets = {}
    for pet_type, pet_weight in args[2:]:
        if available_capacity <= 0:
            all_pets = False
            break

        if pet_weight <= maximum_weight_limit:
            available_capacity -= 1
            pets[pet_type] = pets.get(pet_type, 0) + 1

    output = []
    if all_pets:
        output.append(f"All pets are accommodated! Available capacity: {available_capacity}.")
    else:
        output.append(f"You did not manage to accommodate all pets!")

    output.append("Accommodated pets:")

    for pet, count in sorted(pets.items(), key=lambda x: x[0]):
        output.append(f"{pet}: {count}")

    return "\n".join(output)
