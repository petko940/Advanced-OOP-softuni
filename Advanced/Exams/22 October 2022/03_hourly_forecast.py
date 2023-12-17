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


