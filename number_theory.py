import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = math.isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def prime_factors(n):
    remaining = n
    result = {}
    if n % 2 == 0:
        count = 0
        while remaining % 2 == 0:
            remaining = remaining // 2
            count += 1
        result[2] = count
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if remaining % i == 0:
            count = 0
            while remaining % i == 0:
                remaining = remaining // i
                count += 1
            result[i] = count
    if remaining > 1:
        result[remaining] = 1
    return result


def divisor_count(n):
    factors = prime_factors(n)
    result = 1
    for exponent in factors.values():
        result *= exponent + 1
    return result


def mod_inverse(a, m):  # a.x = 1 (mod m)
    old_r, r = a, m
    old_x, x = 1, 0
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_x, x = x, old_x - quotient * x
    if old_r != 1:
        return None
    return old_x % m
