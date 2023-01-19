regular = set()
vip = set()

for _ in range(int(input())):
    reservation = input()
    if reservation[0].isdigit():
        vip.add(reservation)
    else:
        regular.add(reservation)

while True:
    people_at_party = input()
    if people_at_party == "END":
        break
    if people_at_party[0].isdigit():
        vip.remove(people_at_party)
    else:
        regular.remove(people_at_party)

print(len(regular) + len(vip))
[print(x) for x in sorted(vip)]
[print(x) for x in sorted(regular)]
