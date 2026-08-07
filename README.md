# Number Theory Toolkit

A small practice project: four number theory functions written from scratch in
plain Python 3. The only import is `math.isqrt`, nothing else.

## The functions

### `is_prime(n)`

Primality test with the 6k±1 trick. After ruling out 2 and 3, every prime is
either one less or one more than a multiple of 6, so the loop only checks those
two candidates in each step and stops at `isqrt(n)`. Runs in O(√n).

```python
is_prime(97)    # True
is_prime(91)    # False  (7 * 13)
```

### `prime_factors(n)`

Returns the prime factorization as a `{prime: exponent}` dict. Twos are pulled
out first, then odd divisors up to `isqrt(n)`. Whatever is left above 1 at the
end is itself a prime and goes in with exponent 1.

```python
prime_factors(360)   # {2: 3, 3: 2, 5: 1}
prime_factors(97)    # {97: 1}
```

### `divisor_count(n)`

Counts the divisors of `n` using the factorization: multiply `(e + 1)` over
every exponent. For 360 = 2³ · 3² · 5¹ that is (3+1)·(2+1)·(1+1) = 24.

```python
divisor_count(360)   # 24
```

### `mod_inverse(a, m)`

Finds the `x` with `a · x ≡ 1 (mod m)` using the extended Euclidean algorithm.
The loop carries the remainders alongside the coefficient of `a`, so when the
remainder reaches 1 the coefficient is the inverse. If the last non-zero
remainder (the gcd) is not 1, the inverse does not exist and the function
returns `None`.

```python
mod_inverse(3, 11)   # 4     because 3 * 4 = 12 = 1 (mod 11)
mod_inverse(4, 8)    # None  because gcd(4, 8) = 4
```

## How to run

```bash
python3
>>> from number_theory import is_prime, prime_factors, divisor_count, mod_inverse
>>> divisor_count(360)
24
```
