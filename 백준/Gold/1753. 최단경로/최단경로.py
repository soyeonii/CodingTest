import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
cost = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

heap = []
cost[K] = 0
heappush(heap, (0, K))
while heap:
    c, x = heappop(heap)
    if cost[x] < c:
        continue
    for nc, nx in graph[x]:
        if cost[nx] > c + nc:
            cost[nx] = c + nc
            heappush(heap, (cost[nx], nx))

for c in cost[1:]:
    print(c if c != INF else "INF")