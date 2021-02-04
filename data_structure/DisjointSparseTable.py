class DisjointSparseTable:
    def __init__(self, vector, op):
        self.vector = vector
        self.op = op
        vs = len(vector)
        n = vs.bit_length() - (vs.bit_length() != (vs-1).bit_length())
        self.value = [vector] + [[0] * vs for i in range(n-1)]
        for i in range(1, n):
            s = 1 << i
            j = 0
            while j < vs:
                m = min(j + s, vs)
                self.value[i][m - 1] = vector[m - 1]
                for k in range(m-2, j-1, -1):
                    self.value[i][k] = self.op(self.vector[k], self.value[i][k+1])
                if vs <= m:
                    break
                self.value[i][m] = self.vector[m]
                r = min(m + s, vs)
                for k in range(m+1, r):
                    self.value[i][k] = self.op(self.value[i][k-1], self.vector[k])
                j += s << 1

    def query(self, l, r):
        if l == r:
            return self.vector[l]
        p = -len(self.value) + (l ^ r).bit_length() - 1
        return self.op(self.value[p][l], self.value[p][r])
   
