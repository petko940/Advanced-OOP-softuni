def movie_organizer(*args):
    collection = {}
    for title, genre in args:
        collection[genre] = collection.get(genre, [])
        collection[genre].append(title)

    output = []
    for key, value in sorted(collection.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f'{key} - {len(value)}')
        for v in sorted(value):
            output.append(f"* {v}")

    return '\n'.join(output)
