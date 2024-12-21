def plant_garden(available_space, *allowed_plants, **plant_requests):
    plant_space_requirements = {plant: space for plant, space in allowed_plants}

    sorted_requests = sorted(plant_requests.items())

    planted = {}

    for plant_type, quantity in sorted_requests:
        if plant_type in plant_space_requirements:
            space_per_plant = plant_space_requirements[plant_type]
            max_plants_that_fit = int(available_space // space_per_plant)
            plants_to_plant = min(quantity, max_plants_that_fit)

            if plants_to_plant > 0:
                planted[plant_type] = plants_to_plant
                available_space -= plants_to_plant * space_per_plant

            if available_space <= 0:
                break

    all_planted = True
    for plant in sorted_requests:
        if plant[0] in plant_space_requirements and planted.get(plant[0], 0) < plant[1]:
            all_planted = False
            break

    result = []
    if all_planted:
        result.append(f"All plants were planted! Available garden space: {available_space:.1f} sq meters.")
    else:
        result.append("Not enough space to plant all requested plants!")

    if planted:
        result.append("Planted plants:")
        for plant_type in sorted(planted):
            result.append(f"{plant_type}: {planted[plant_type]}")

    return '\n'.join(result)


print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))
