from collections import deque

peaks = {
    1: ['Vihren', 80],
    2: ['Kutelo', 90],
    3: ['Banski Suhodol', 100],
    4: ['Polezhan', 60],
    5: ['Kamenitza', 70],
}

food_portions = deque([int(x) for x in input().split(', ')])
stamina = deque([int(x) for x in input().split(', ')])

conquered_peaks = []
count = 1

while food_portions and stamina and len(conquered_peaks) != 5:
    last_food = food_portions.pop()
    first_stamina = stamina.popleft()
    sum = last_food + first_stamina
    if sum >= peaks[count][1]:
        conquered_peaks.append(peaks[count][0])
        count += 1

if count == 6:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    [print(x) for x in conquered_peaks]
