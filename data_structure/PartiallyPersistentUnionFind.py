class PartiallyPersistentUnionFind:
    def __init__(self, n):
        self.now = 0
        self.time = [None] * n
        self.count = [[] for i in range(n)]
        self.count_time = [[] for i in range(n)]
        self.__n = n
        self.__parents = [-1] * n

    def union(self, x, y):
        self.now += 1
        x, y = self.find(x, self.now), self.find(y, self.now)
        if x != y:
            if self.__parents[x] > self.__parents[y]:
                x, y = y, x
            self.count_time[x] += [self.now]
            self.count[x] += [self.size(x, self.now) + self.size(y, self.now)]
            self.__parents[x] += self.__parents[y]
            self.__parents[y] = x
            self.time[y] = self.now

    def find(self, x, t):
        while t >= self.time[x]:
            x = self.__parents[x]
        return x

    def size(self, x, t):
        return self.count[self.find(x, t)][bisect.bisect_right(self.count_time, t)-1]

    def same(self, x, y, t):
         return self.find(x, t) == self.find(y, t)

    def members(self, x, t):
        root = self.find(x, t)
        return [i for i in range(len(self.__parents)) if self.find(i, t) == root]
