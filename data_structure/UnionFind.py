class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1 for i in range(n)]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.parents[x] > self.parents[y]:
                x, y = y, x
            self.parents[x] += self.parents[y]
            self.parents[y] = x

    def find(self, x):
        y = x
        while self.parents[x] >= 0:
            x = self.parents[x]
        while y != x:
            t = y
            y = self.parents[y]
            self.parents[t] = x
        return x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
         return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(len(self.parents)) if self.find(i) == root]

    def roots(self):
        ans = []
        for i in range(self.n):
            if self.parents[i] < -1:
                ans += [i]
        return ans

    def group_count(self):
        return len(self.roots())

    def max_size(self):
        return -min(self.parents)

    def min_size(self):
        return -max(self.roots())

    def append(self, n):
        self.parents += [-1 for i in range(n)]
