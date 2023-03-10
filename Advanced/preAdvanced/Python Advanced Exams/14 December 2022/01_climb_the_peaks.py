from collections import deque

food_portions = deque([int(x) for x in input().split(", ")])
stamina = deque([int(x) for x in input().split(", ")])

peaks = {
    1: ["Vihren", 80],
    2: ["Kutelo", 90],
    3: ["Banski Suhodol", 100],
    4: ["Polezhan", 60],
    5: ["Kamenitza", 70]
}
peak = []
count = 0
taken_peak = 0
while count < 5 and food_portions and stamina:
    count += 1
    last_daily_food = food_portions.pop()
    first_daily_stamina = stamina.popleft()
    sum_last_first = last_daily_food + first_daily_stamina
    if sum_last_first >= peaks[count][1]:
        peak.append(peaks[count][0])
        taken_peak += 1
    else:
        count -= 1
        if count < taken_peak:
            count = taken_peak

if count == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if peak:
    print("Conquered peaks:")
    [print(x) for x in peak]
