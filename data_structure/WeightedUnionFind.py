# UnionFindが前提
class WeightedUnionFind(UnionFind):
    def __init__(self, n):
        self.__weight = [0] * n
        self.__n = n
        self.__parents = [-1] * n

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
