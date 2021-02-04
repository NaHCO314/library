class BinaryIndexedTree:
    def __init__(self, n):
        self.__data, self.__n = [0] * n, n

    def add(self, p, x):
        p += 1
        while p <= self.__n:
            self.__data[p - 1] += x
            p += p & -p

    def sum(self, l, r):
        return self.__sum(r) - self.__sum(l)

    def __sum(self, r):
        s = 0
        while r:
            s += self.__data[r - 1]
            r -= r & -r
        return s
