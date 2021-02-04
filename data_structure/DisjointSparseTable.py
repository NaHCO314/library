class DisjointSparseTable:
    def __init__(self, vector, op):
        self.__vector = vector
        self.__op = op
        vs = len(vector)
        n = vs.bit_length() - (vs.bit_length() != (vs - 1).bit_length())
        self.__value = [vector] + [[0] * vs for i in range(n - 1)]
        for i in range(1, n):
            s = 1 << i
            j = 0
            while j < vs:
                m = min(j + s, vs)
                self.__value[i][m - 1] = vector[m - 1]
                for k in range(m - 2, j - 1, -1):
                    self.__value[i][k] = self.__op(self.__vector[k], self.__value[i][k + 1])
                if vs > m:
                    self.__value[i][m] = self.__vector[m]
                    for k in range(m + 1, min(m + s, vs)):
                        self.__value[i][k] = self.__op(self.__value[i][k - 1], self.__vector[k])
                j += s << 1

    def query(self, l, r):
        if l == r:
            return self.__vector[l]
        p = -len(self.__value) + (l ^ r).bit_length() - 1
        return self.__op(self.__value[p][l], self.__value[p][r])
