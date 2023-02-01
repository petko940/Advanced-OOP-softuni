def forecast(*args):
    data = {"Sunny": [], "Cloudy": [], "Rainy": []}
    for location, weather in args:
        data[weather].append(location)

    output = []
    for key, value in data.items():
        if value:
            for v in sorted(value):
                output.append(f"{v} - {key}")
    return '\n'.join(output)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
