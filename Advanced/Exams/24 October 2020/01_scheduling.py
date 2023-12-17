jobs = [int(x) for x in input().split(", ")]
index = int(input())

data = {}
for i in range(len(jobs)):
    data[i] = jobs[i]

sorted_data = sorted(data.items(), key=lambda x: x[1])

count = 0
for idx in sorted_data:
    if index == idx[0]:
        count += idx[1]
        print(count)
        break
    count += idx[1]
