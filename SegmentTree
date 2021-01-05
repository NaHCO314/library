class SegmentTree:
    def __init__(self, n, op, identity=None):
        self.op = op
        self.identity = identity
        if self.identity is None:
            self.identity = 1
            if op in [operator.add, operator.sub, LCM, operator.or_, operator.xor]:
                self.identity = 0
            elif op == min:
                self.identity = float("INF")
            elif op == max:
                self.identity = -format("INF")
        if type(n) == int:
            self.n = 2 ** math.ceil(math.log(n, 2))
            self.val = [self.identity] * self.n * 2
        else:
            self.n = 2 ** math.ceil(math.log(len(n), 2))
            self.val = [self.identity] * self.n + n + [self.identity] * (self.n - len(n))
            for i in range(self.n - 1, -1, -1):
                self.val[i] = self.op(self.val[2 * i], self.val[2 * i + 1])
        self.range = [None] * self.n * 2
        for i in range(self.n):
            self.range[i + self.n] = [i, i+1]
        for i in range(self.n - 1, 0, -1):
            self.range[i] = [self.range[i<<1][0], self.range[(i<<1)+1][1]]

    def update(self, i, x, func=lambda n, m: m):
        i += self.n - 1
        self.val[i] = func(self.val[i], x)
        while i > 0:
            i >>= 1
            self.val[i] = self.op(self.val[i<<1], self.val[(i<<1) + 1])

    def query(self, l, r):
        l += self.n - 1
        r += self.n
        ans = self.identity
        while l < r:
            if l & 1:
                ans = self.op(ans, self.val[l])
                l += 1
            if r & 1:
                r -= 1
                ans = self.op(self.val[r], ans)
            l >>= 1
            r >>= 1
        return ans

    def bisect(self, l, r, var=None, func=None):
        if func is var is None:
            val, l, r, func = l, 0, self.n+1, r
        ret, off = self.identity, l
        l += self.n
        while l < 2*self.n and off < r:
            if self.range[l][1] <= r and (not func(self.op(ret, self.val[l]), var)):
                ret = self.op(ret, self.val[l])
                off = self.range[l][1]
                l += 1
                if not l & 1:
                    l >>= 1
            else:
                l <<= 1
        return off
