from collections import deque

jobs = deque([int(x) for x in input().split(", ")])
index = int(input())

sorted_jobs = sorted(jobs)
cycles = 0
is_done = False
while not is_done:
    for idx, value in enumerate(jobs):
        if jobs[idx] == sorted_jobs[0]:
            if idx == index:
                cycles += jobs[idx]
                is_done = True
            else:
                cycles += jobs[idx]
            del sorted_jobs[0]
            jobs[idx] = 0
            break

print(cycles)
