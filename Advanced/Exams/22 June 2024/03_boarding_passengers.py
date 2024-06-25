def boarding_passengers(capacity, *args):
    data = {}

    for number_passengers, benefits in args:
        if number_passengers <= capacity:
            capacity -= number_passengers
            data[benefits] = data.get(benefits, 0) + number_passengers

    sorted_data = ["Boarding details by benefit plan:"]
    for key, value in sorted(data.items(), key=lambda x: (-x[1], x[0])):
        sorted_data.append(f"## {key}: {value} guests")

    total_boarded_passengers = sum(data.values())
    total_requested_passengers = sum(num for num, _ in args)

    if total_boarded_passengers == total_requested_passengers:
        sorted_data.append("All passengers are successfully boarded!")
    elif capacity == 0:
        sorted_data.append("Boarding unsuccessful. Cruise ship at full capacity.")
    else:
        sorted_data.append(f"Partial boarding completed. Available capacity: {capacity}.")

    return '\n'.join(sorted_data)

