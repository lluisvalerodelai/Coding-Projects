
def factorial(n):
    assert n >= 0 and type(n) == int
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)


def fibbonacci(n):
    assert n >= 0 and type(n) == int
    if n in [0, 1]:
        return n
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)


def sumDigits(n):
    assert n > 0 and type(n) == int, "number must be positive integer"
    if n == 0:
        return 0
    else:
     return int(n%10) + sumDigits(int(n/10))


def power(base, exp):
    assert exp >= 0 and type(exp) == int, "exponent must be positive integer"
    
    if exp == 1:
        return base
    else:
        return base * power(base, exp-1)


def gcd(a, b):
    assert type(a and b) == int
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def decimalToBinary(n):

    assert type(n) == int, "n must be an integer"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(int(n/2))


