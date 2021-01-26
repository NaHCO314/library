import math

gcd = math.gcd


def lcm(n, m):
    return (n * m) // gcd(n, m)


def div(n):
    l, u = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            l.append(i)
            if i != n // i:
                u.append(n // i)
        i += 1
    return l + u[::-1]
# 約数のリスト


def prime(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
# 素因数分解のリスト


def C(n, r):
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def P(n, r):
    if n < r:
        return 0
    return math.factorial(n) // math.factorial(n - r)


def H(n, r):
    return C(n + r - 1, r)
