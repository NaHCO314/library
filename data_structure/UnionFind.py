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
