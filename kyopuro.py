# 競プロ関連のあれこれ
def bits(n):
    for i in range(1<<n):
        yield list(map(int, str(bin(i))[2:].zfill(n)))


def trisect(f, *, r=10**10, e=0.000000001):
    l = 0
    while r - l >= e:
        if f((2 * l + r) / 3) < f((l + 2 * r) / 3):
            r = (l + 2 * r) / 3
        else:
            l = (2 * l + r) / 3
    return l
    
