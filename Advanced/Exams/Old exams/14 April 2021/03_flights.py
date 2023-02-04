def flights(*args):
    data = {}
    for n in range(0, len(args), 2):
        if args[n] == "Finish":
            break
        destination = args[n]
        passengers = args[n + 1]
        data[destination] = data.get(destination, 0) + passengers

    return data


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
