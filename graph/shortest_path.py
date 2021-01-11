def dijkstra(g, s):
    n = len(g)
    dist = [INF] * n
    hq = [(0, s)]
    dist[s] = 0
    seen = [False] * n
    while hq:
        v = heapq.heappop(hq)[1]
        seen[v] = True
        for to, cost in g[v]:
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heapq.heappush(hq, (dist[to], to))
    return dist

# 隣接リスト [[[ノード, コスト]...]...]
