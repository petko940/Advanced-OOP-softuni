from collections import deque

tools = [int(x) for x in input().split()]
substances = deque([int(x) for x in input().split()])
challenges = [int(x) for x in input().split()]

while tools and substances:
    first_tool = tools.pop(0)
    last_substance = substances.pop()

    result = first_tool * last_substance
    if result in challenges:
        challenges.remove(result)
    else:
        tools.append(first_tool + 1)

        if last_substance - 1 > 0:
            substances.append(last_substance - 1)

    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")

if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")

if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")