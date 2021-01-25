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

    def members(self, x):
        root = self.find(x)
        return [i for i in range(len(self.__parents)) if self.find(i) == root]

    def roots(self):
        ans = []
        for i in range(self.__n):
            if self.__parents[i] < -1:
                ans += [i]
        return ans

    def group_count(self):
        return len(self.roots())

    def max_size(self):
        return -min(self.__parents)

    def min_size(self):
        return -max(self.roots())


class WeightedUnionFind(UnionFind):
    def __init__(self, n):
        self.__weight = [0] * n
        self.__n = n
        self.__parents = [-1 for i in range(n)]

    def union(self, x, y, w):
        w += self.weight(x) - self.weight(y)
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.__parents[x] > self.__parents[y]:
                x, y, w = y, x, -w
            self.__parents[x] += self.__parents[y]
            self.__parents[y], self.__weight[y] = x, w

    def find(self, x):
        s = []
        while self.__parents[x] >= 0:
            s += [x]
            x = self.__parents[x]
        for i in s[::-1]:
            self.__weight[i] += self.__weight[self.__parents[i]]
            self.__parents[i] = x
        return x

    def weight(self, x):
        self.find(x)
        return self.__weight[x]

    def diff(self, x, y):
        return self.weight(y) - self.weight(x)
