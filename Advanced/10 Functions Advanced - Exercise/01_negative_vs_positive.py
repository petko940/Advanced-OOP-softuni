def negative(negatives):
    negatives = [x for x in negatives if x < 0]
    return negatives


def positive(positives):
    positives = [x for x in positives if x > 0]
    return positives


def result():
    print(sum(negative(numbers)))
    print(sum(positive(numbers)))
    if abs(sum(negative(numbers))) > sum(positive(numbers)):
        return "The negatives are stronger than the positives"
    return "The positives are stronger than the negatives"


numbers = [int(x) for x in input().split()]
print(result())
