import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    queue = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        x = queue.popleft()
        result.append(x)

        for nx in graph[x]:
            indegree[nx] -= 1
            if indegree[nx] == 0:
                queue.append(nx)

    return result

print(*topology_sort())