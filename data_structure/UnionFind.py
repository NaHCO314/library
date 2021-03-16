class UnionFind:
    def __init__(self, n):
        self.__n = n
        self.__parents = [-1] * n

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.__parents[x] > self.__parents[y]:
                x, y = y, x
            self.__parents[x] += self.__parents[y]
            self.__parents[y] = x

    def find(self, x):
        y = x
        while self.__parents[x] >= 0:
            x = self.__parents[x]
        while y != x:
            t = y
            y = self.__parents[y]
            self.__parents[t] = x
        return x

    def size(self, x):
        return -self.__parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)
