import sys
from collections import deque


def BFS(v):
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        for nv in graph[v]:
            if visited[nv] == False:
                visited[nv] = True
                queue.append(nv)


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
for i in range(1, n + 1):
    if visited[i] == False:
        BFS(i)
        result += 1

print(result)