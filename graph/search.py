def DFS(g, s, pos=None):
    if pos is None:
        pos = set()
    pos.add(s)
    for i in g[s]:
        if not (i in pos):
            DFS(g, i, pos)
    return pos


def BFS(g, s):
    q, pos = collections.deque([s]), set([s])
    while q:
        s = q.pop()
        for i in g[s]:
            if i not in pos:
                pos.add(i)
                q.append(i)
    return pos

# 隣接リスト
# D/BFS(グラフ, スタート地点)
# 戻り値はスタート地点と連結している要素のset

