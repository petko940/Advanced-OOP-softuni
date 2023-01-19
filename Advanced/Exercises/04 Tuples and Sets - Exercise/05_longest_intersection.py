class LongestIntersection:
    def __init__(self, number):
        self.number = number
        self.longest_intersection = []

    def check(self):
        for _ in range(self.number):
            ranges = [x for x in input().split("-")]
            first_range = [int(x) for x in ranges[0].split(",")]
            first_set = {x for x in range(first_range[0], first_range[1] + 1)}
            second_range = [int(x) for x in ranges[1].split(",")]
            second_set = {x for x in range(second_range[0], second_range[1] + 1)}
            intersection = first_set.intersection(second_set)
            if len(intersection) > len(self.longest_intersection):
                self.longest_intersection = intersection

    def __repr__(self):
        output = list(self.longest_intersection)
        return f"Longest intersection is [{', '.join([str(x) for x in output])}] with length {len(self.longest_intersection)}"


num = LongestIntersection(int(input()))
num.check()
print(num)
