from collections import deque

armor_values_monsters = deque([int(x) for x in input().split(',')])
soldier_striking = deque([int(x) for x in input().split(',')])
killed_monsters = 0

all_monsters = len(armor_values_monsters)
while armor_values_monsters and soldier_striking:
    armor = armor_values_monsters.popleft()
    strike = soldier_striking.pop()

    if strike >= armor:
        strike -= armor
        killed_monsters += 1

        if strike:
            if soldier_striking:
                soldier_striking[-1] += strike

            elif not soldier_striking:
                soldier_striking.append(strike)
    else:
        armor_values_monsters.append(armor - strike)

if all_monsters == killed_monsters:
    print(f"All monsters have been killed!")

if not soldier_striking:
    print(f"The soldier has been defeated.")

print(f'Total monsters killed: {killed_monsters}')
