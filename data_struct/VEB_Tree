class VEB:
    def __init__(self, u, original_list=None):
        self.min = None
        self.max = None
        self.u = 2
        while self.u < u:
            self.u = self.u * self.u
        if u > 2:
            self.cluster = [None for i in range(self.bin(self.u)[0])]
            self.summary = None
        if original_list:
            for i in original_list:
                self.insert(i)

    def __str__(self):
        return str(self.list())

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, item):
        return self.member(item)

    def __iter__(self):
        self.iter = -1
        return self

    def __next__(self):
        if self.iter == self.max:
            raise StopIteration
        self.iter = self.next(self.iter)
        return self.iter

    def bin(self, x):
        return int(math.floor(x / math.sqrt(self.u))), int(x % math.ceil(math.sqrt(self.u)))

    def index(self, x, y):
        return int(x * math.floor(math.sqrt(self.u)) + y)

    def member(self, x):
        if self.min == x or self.max == x:
            return True
        if self.u <= 2:
            return False
        c, i = self.bin(x)
        cluster_of_x = self.cluster[c]
        if cluster_of_x is not None:
            return cluster_of_x.member(i)
        return False

    def earlier(self, x):
        if self.u <= 2:
            if x == 1 and self.min == 0:
                return 0
            return None
        if self.max is not None and x > self.max:
            return self.max
        else:
            c, i = self.bin(x)
            high_cluster = self.cluster[c]
            min_low = None
            if high_cluster is not None:
                min_low = high_cluster.min
            if (min_low is not None) and (i > min_low):
                offset = high_cluster.earlier(i)
                if offset is not None:
                    return self.index(c, offset)
                return self.index(c, 0)
            pred_cluster = None
            if self.summary is not None:
                pred_cluster = self.summary.earlier(c)
            if pred_cluster is None:
                if (self.min is not None) and (x > self.min):
                    return self.min
                return None
            if self.cluster[pred_cluster] is not None:
                offset = self.cluster[pred_cluster].max
            if offset is not None:
                return self.index(pred_cluster, offset)
            return self.index(pred_cluster, 0)

    def next(self, x):
        if self.u <= 2:
            if x == 0 and self.max == 1:
                return 1
            return None
        elif self.min is not None and x < self.min:
            return self.min
        else:
            c, i = self.bin(x)
            high_cluster = self.cluster[c]
            max_low = None
            if high_cluster is not None:
                max_low = high_cluster.max
            if (max_low is not None) and (i < max_low):
                offset = high_cluster.next(i)
                return self.index(c, offset)
            succ_cluster = None
            if self.summary is not None:
                succ_cluster = self.summary.next(c)
            if succ_cluster is None:
                return None
            offset = 0
            if self.cluster[succ_cluster] is not None:
                offset = self.cluster[succ_cluster].min
            return self.index(succ_cluster, offset)

    def insert(self, x):
        if self.min is None:
            self.min = self.max = x
        else:
            if x < self.min:
                self.min, x = x, self.min
            if self.u > 2:
                c, i = self.bin(x)
                if self.cluster[c] is None:
                    self.cluster[c] = VEB(self.bin(self.u)[0])
                if self.summary is None:
                    self.summary = VEB(self.bin(self.u)[0])
                if self.cluster[c].min is None:
                    self.summary.insert(c)
                    self.cluster[c].min = self.cluster[c].max = i
                else:
                    self.cluster[c].insert(i)
            if x > self.max:
                self.max = x

    def delete(self, x):
        if self.min == self.max:
            self.min = self.max = None
        elif self.u == 2:
            self.min = 1 if x == 0 else 0
            self.max = self.min
        else:
            if x == self.min:
                first_cluster = self.summary.min
                self.min = x = self.index(first_cluster, self.cluster[first_cluster].min)
            c, i = self.bin(x)
            self.cluster[c].delete(i)
            if self.cluster[c].min is None:
                self.summary.delete(c)
                if x == self.max:
                    summary_max = self.summary.max
                    if summary_max is None:
                        self.max = self.min
                    else:
                        self.max = self.index(summary_max, self.cluster[summary_max].max)
            elif x == self.max:
                self.max = self.index(c, self.cluster[c].max)
        return x

    def pop(self):
        return self.delete(self.max)

    def popmin(self):
        return self.delete(self.min)

    def list(self):
        return [i for i in self]
