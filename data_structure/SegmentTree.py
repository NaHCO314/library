import operator     


class SegmentTree:
    def __init__(self, n, op, identity=None):
        self.__op = op
        self.__identity = identity
        if self.__identity is None:
            self.__identity = 1
            if op in [operator.add, operator.sub, operator.or_, operator.xor]:
                self.__identity = 0
            elif op == min:
                self.__identity = float("INF")
            elif op == max:
                self.__identity = -float("INF")
        if type(n) == int:
            self.__n = 1 << (n.bit_length() - (n.bit_length() != (n - 1).bit_length()))
            self.__val = [self.__identity] * self.__n * 2
        else:
            self.__n = 1 << (len(n).bit_length() - (len(n).bit_length() != (len(n) - 1).bit_length()))
            self.__val = [self.__identity] * self.__n + n + [self.__identity] * (self.__n - len(n))
            for i in range(self.__n - 1, -1, -1):
                self.__val[i] = self.__op(self.__val[2 * i], self.__val[2 * i + 1])
        self.__range = [None] * self.__n * 2
        for i in range(self.__n):
            self.__range[i + self.__n] = [i, i + 1]
        for i in range(self.__n - 1, 0, -1):
            self.__range[i] = [self.__range[i << 1][0], self.__range[(i << 1) + 1][1]]

    def update(self, i, x, func=lambda n, m: m):
        i += self.__n - 1
        self.__val[i] = func(self.__val[i], x)
        while i > 0:
            i >>= 1
            self.__val[i] = self.__op(self.__val[i << 1], self.__val[(i << 1) + 1])

    def query(self, l, r):
        l += self.__n - 1
        r += self.__n
        ans = self.__identity
        while l < r:
            if l & 1:
                ans = self.__op(ans, self.__val[l])
                l += 1
            if r & 1:
                r -= 1
                ans = self.__op(self.__val[r], ans)
            l >>= 1
            r >>= 1
        return ans

    def bisect(self, l, r, var=None, func=None):
        if func is var is None:
            val, l, r, func = l, 0, self.__n + 1, r
        ret, off = self.__identity, l
        l += self.__n
        while l < 2*self.__n and off < r:
            if self.__range[l][1] <= r and (not func(self.__op(ret, self.__val[l]), var)):
                ret = self.__op(ret, self.__val[l])
                off = self.__range[l][1]
                l += 1
                if not l & 1:
                    l >>= 1
            else:
                l <<= 1
        return off
