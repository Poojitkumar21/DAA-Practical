import heapq
def prim(graph):
    n = len(graph)
    visited = [False] * n
    pq = [(0, 0)]
    mst = []
    total = 0

    while pq:
        weight, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True
        total += weight

        if weight != 0:
            mst.append((u, weight))

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))

    return total, mst


graph = [
    [(1, 2), (3, 6)],
    [(0, 2), (2, 3), (3, 8), (4, 5)],
    [(1, 3), (4, 7)],
    [(0, 6), (1, 8), (4, 9)],
    [(1, 5), (2, 7), (3, 9)]
]
cost, mst = prim(graph)

print("Minimum cost:", cost)
print("MST:", mst)
