def DFS(g, s, pos=None):
    if pos is None:
        pos = set()
    pos.add(s)
    for i in g[s]:
        if not (i in pos):
            DFS(g, i, pos)
    return pos


def DFS_one(g, s, pos=None):
    if pos is None:
        pos = set()
    pos = copy(pos)
    pos.add(s)
    b = copy(pos)
    m = copy(pos)
    for i in g[s]:
        if not (i in pos):
            b = DFS(g, i, pos)
            if len(m) < len(b):
                m = b
    return m


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
