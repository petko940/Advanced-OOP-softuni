from collections import deque

strengths = deque([int(x) for x in input().split()])
accuracies = deque([int(x) for x in input().split()])
goals = 0

while strengths and accuracies:
    strength = strengths.pop()
    accuracy = accuracies.popleft()

    sum = strength + accuracy

    if sum == 100:
        goals += 1

    elif sum < 100:
        if strength < accuracy:
            accuracies.appendleft(accuracy)
        elif strength > accuracy:
            strengths.append(strength)
        else:
            strengths.append(sum)

    else:
        strength -= 10
        strengths.append(strength)
        accuracies.append(accuracy)

if goals == 3:
    print("Paul scored a hat-trick!")
elif not goals:
    print("Paul failed to score a single goal.")
elif goals > 3:
    print("Paul performed remarkably well!")
elif 0 < goals < 3:
    print("Paul failed to make a hat-trick.")

if goals:
    print(f"Goals scored: {goals}")

if strengths:
    print(f"Strength values left: {', '.join([str(x) for x in strengths])}")

if accuracies:
    print(f"Accuracy values left: {', '.join([str(x) for x in accuracies])}")
