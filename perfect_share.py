import math


# Check whether the number is prime or not
def is_prime(number):
    if number > 1:
        for divisor in range(2, int(math.sqrt(number))+1):
            if (number % divisor) == 0:
                return False
        return True
    else:
        return False


# This function uses the Lucas–Lehmer primality test.
# More information can be found here:
# https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test
def is_mersenne_prime(prime, mersenne_prime):
    sequence = 4
    for i in range(prime - 2):
        sequence = (sequence * sequence - 2) % mersenne_prime
    if sequence == 0:
        return True
    else:
        return False


# In this function I used the fact that according to Euclid:
# (2**p-1) * (2**p) - 1 is a perfect number whenever (2**p) - 1 is prime.
# Prime numbers of the form (2**p) - 1 are called mersenne primes.
# Additional information can be found here: https://en.wikipedia.org/wiki/Perfect_number
def perfect_share():
    yield 6  # First case to simplify the solution.
    prime_number = 3  # The next prime number is 3 (2 yields 6).
    while True:
        if is_mersenne_prime(prime_number, 2 ** prime_number - 1):
            yield 2 ** (2 * prime_number - 1) - 2 ** (prime_number - 1)
        while True:
            prime_number += 2  # next potential prime number
            if is_prime(prime_number):
                break


generator_iterator = perfect_share()
for perfect_number in generator_iterator:
    print(perfect_number)
