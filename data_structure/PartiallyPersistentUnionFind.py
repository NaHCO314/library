import bisect


class PartiallyPersistentUnionFind:
    def __init__(self, n):
        self.__now = 0
        self.__time = [None] * n
        self.__count = [[] for i in range(n)]
        self.__count_time = [[] for i in range(n)]
        self.__n = n
        self.__parents = [-1] * n

    def union(self, x, y):
        self.__now += 1
        x, y = self.find(x, self.__now), self.find(y, self.__now)
        if x != y:
            if self.__parents[x] > self.__parents[y]:
                x, y = y, x
            self.__count_time[x] += [self.__now]
            self.__count[x] += [self.size(x, self.__now) + self.size(y, self.__now)]
            self.__parents[x] += self.__parents[y]
            self.__parents[y] = x
            self.__time[y] = self.__now

    def find(self, x, t):
        while t >= self.__time[x]:
            x = self.__parents[x]
        return x

    def size(self, x, t):
        return self.__count[self.find(x, t)][bisect.bisect_right(self.__count_time, t) - 1]

    def same(self, x, y, t):
         return self.find(x, t) == self.find(y, t)

    def members(self, x, t):
        root = self.find(x, t)
        return [i for i in range(len(self.__parents)) if self.find(i, t) == root]
