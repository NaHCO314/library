def inv_gcd(n, m):
    n %= m
    if n == 0:
        return m, 0
    s, t = m, n
    m0, m1 = 0, 1
    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u
        s, t, m0, m1 = t, s, m1, m0
    if m0 < 0:
        m0 += m // s
    return s, m0


def is_prime(n):
    if n <= 1 or n % 2 == 0:
        return False
    if n in (2, 7, 61):
        return True
    d = n - 1
    d //= d & -d
    bases = (2, 7, 61)
    for a in bases:
        t, y = d, pow(a, d, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = y * y % n
            t <<= 1
        if y != n - 1 and t % 2 == 0:
            return False
    return True


def primitive_root(m):
    if m == 2:
        return 1
    if m in (167772161, 469762049, 998244353):
        return 3
    if m == 754974721:
        return 11
    divs = [0] * 20
    divs[0] = 2
    cnt, x, i = 1, (m - 1) // 2, 3
    x //= x & -x
    while i*i <= x:
        if x % i == 0:
            divs[cnt] = i
            cnt += 1
            while x % i == 0:
                x //= i
        i += 2
    if x > 1:
        divs[cnt] = x
        cnt += 1
    g = 2
    while True:
        ok = True
        for i in range(cnt):
            if pow(g, (m - 1) / divs[i], m) == 1:
                ok = False
                break
        if ok:
            return g
        g += 1
