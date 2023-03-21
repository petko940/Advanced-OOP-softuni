def get_primes(numbers):
    for n in numbers:
        if n < 2:
            continue

        for x in range(2, n):
            if n % x == 0:
                break
        else:
            yield n
