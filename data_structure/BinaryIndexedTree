class BinaryIndexedTree:
    def __init__(self, n):
        self.data, self.n = [9] * n, n

    def add(self, p, x):
        p += 1
        while p <= self.n:
            self.data[p-1] += x
            p += p & -p

    def sum(self, l, r):
        return self.__sum(r) - self.__sum(l)

    def __sum(self, r):
        s = 0
        while r:
            s += self.data[r - 1]
            r -= r & -r
        return s
