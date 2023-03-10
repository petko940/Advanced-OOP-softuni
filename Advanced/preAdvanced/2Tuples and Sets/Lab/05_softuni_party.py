number_guests = int(input())

regular = set()
vip = set()

for _ in range(number_guests):
    reservation = input()
    if reservation[0].isdigit():
        vip.add(reservation)
    else:
        regular.add(reservation)

while True:
    guest_to_party = input()
    if guest_to_party == "END":
        break
    if guest_to_party[0].isdigit():
        vip.remove(guest_to_party)
    else:
        regular.remove(guest_to_party)

output = list(sorted(vip)) + list(sorted(regular))
print(len(output))
print('\n'.join(output))
