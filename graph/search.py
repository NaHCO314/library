def DFS(g, s, pos=None):
    if pos is None:
        pos = set()
    pos.add(s)
    for i in g[s]:
        if not (i in pos):
            DFS(g, i, pos)
    return pos


def BFS(g, q, pos=None):
    if pos is None:
        pos = set()
    if type(q) == deque:
        pos.add(q)
        q = deque([q])
    pos.add(q[-1])
    for i in g[q.pop()]:
        if not i in pos:
            q.append(i)
    while q != deque():
        pos, q = BFS(g, q, pos)
    return pos, q
