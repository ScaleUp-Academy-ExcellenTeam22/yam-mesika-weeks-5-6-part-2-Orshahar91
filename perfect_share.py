def is_prime(num):
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False


def is_mersenne_prime(prime, mersenne_prime):
    n = 4
    for i in range(prime - 2):
        n = (n * n - 2) % mersenne_prime
    if n == 0:
        return True
    else:
        return False


def perfect_share():
    yield 6
    p = 3
    while True:
        if is_mersenne_prime(p, 2 ** p - 1):
            yield 2 ** (2 * p - 1) - 2 ** (p - 1)
        while True:
            p += 2
            if is_prime(p):
                break


generator_iterator = perfect_share()
for number in generator_iterator:
    print(number)
