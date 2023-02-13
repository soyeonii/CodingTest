from collections import deque
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())
    count = 0
    queue = deque()
    visited = [False] * (N + 1)
    visited[v] = True
    queue.append((v, float('inf')))
    while queue:
        x, c = queue.pop()
        for nx, nc in graph[x]:
            nc = min(c, nc)
            if not visited[nx] and k <= nc:
                count += 1
                visited[nx] = True
                queue.append((nx, nc))
    print(count)