def forecast(*args):
    info = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": []
    }
    for location, weather in args:
        info[weather].append(f"{location} - {weather}")

    output = ""
    for value in sorted(info["Sunny"]):
        output += f"{value}\n"
    for value in sorted(info["Cloudy"]):
        output += f"{value}\n"
    for value in sorted(info["Rainy"]):
        output += f"{value}\n"
    return output


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
