def dijkstra(g, s):
    n = len(g)
    dist = [float("INF")] * n
    dist[s] = 0
    q = [(0, s)]
    seen = [False] * n
    while q:
        v = heapq.heappop(q)[1]
        seen[v] = True
        for i, j in g[v]:
            if seen[i] == False and dist[v] + j < dist[i]:
                dist[i] = dist[v] + j
                heapq.heappush(q, (dist[i], i))
    return dist

# dijkstra(グラフ, 開始地点)
# 戻り値はリストで、[i]にはiまでの最短コストがある
# 隣接リスト [[[ノード, コスト]...]...]
# O((E+V) log V)

def BFS(g, s):
    dist = [float("INF")] * len(g)
    dist[s] = 0
    q, pos = collections.deque([s]), set([s])
    while q:
        s = q.popleft()
        for i in g[s]:
            if i not in pos:
                dist[i] = dist[s] + 1
                pos.add(i)
                q.append(i)
    return dist

# BFS(グラフ、開始地点)
# 戻り値はリストで、[i]にはiまでの最短距離がある
# 隣接リスト [[ノード...]...]
# O(E)
