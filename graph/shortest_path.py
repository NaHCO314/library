def dijkstra(g, s):
    n = len(g)
    dist = [float("INF")] * n
    dist[s] = 0
    hq = [(0, s)]
    seen = [False] * n
    while hq:
        v = heapq.heappop(hq)[1]
        seen[v] = True
        for to, cost in g[v]:
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heapq.heappush(hq, (dist[to], to))
    return dist

# dijkstra(グラフ, 開始地点)
# 戻り値はリストで、[i]にはiまでの最短コストがある
# 隣接リスト [[[ノード, コスト]...]...]
# O(V^2)
