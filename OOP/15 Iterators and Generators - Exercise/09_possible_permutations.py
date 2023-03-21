from itertools import permutations


def possible_permutations(items):
    for i in list(permutations(items)):
        yield list(i)
