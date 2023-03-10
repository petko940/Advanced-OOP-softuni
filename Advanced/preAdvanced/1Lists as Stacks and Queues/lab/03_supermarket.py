clients = []

while True:
    name = input()
    if name == 'End':
        print(f"{len(clients)} people remaining.")
        break

    if name == 'Paid':
        for x in clients:
            print(x)
        clients.clear()
        continue
    clients.append(name)
