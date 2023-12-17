def team_lineup(*args):
    result = {}
    for name, country in args:
        result[country] = result.get(country, [])
        result[country].append(name)

    output = []
    for country, names in sorted(result.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f"{country}:")
        for n in names:
            output.append(f"  -{n}")

    return "\n".join(output)
