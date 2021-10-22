"""


@author: radu

Problem 1
a) Compute the sum of the first n natural numbers.
b) Check if a given integer number n is prime.
c) Compute the greatest common divisor between two integers a and b.
d) Compute the first prime number greater than a given integer n.
e) Print the first k prime numbers greater than a given integer n.
"""
from math import sqrt


def sum_of_first_naturals(n):
    """Computes the sum of the first n natural numbers.

    Given a natural number [n], compute the sum of the first [n] natural numbers.

    :param n: natural number
    :return: the sum of the first [n] natural numbers.
    """
    s = 0
    for i in range(n):
        s += i
    return s


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def next_prime(n):
    while True:
        n = n + 1
        if is_prime(n):
            return n


def print_next_k_primes(n, k):
    for i in range(k):
        n = next_prime(n)
        print(n)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a if a > 0 else -a


if __name__ == '__main__':
    pass
    # print(sum_of_first_naturals(3))
    # for i in range(20):
    #     print(i, " ", is_prime(i))
    # print(gcd(12, -8))
    # print(next_prime(7))
    # print_next_k_primes(7,4)
