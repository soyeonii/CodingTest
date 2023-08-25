import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    size = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and not graph[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    size += 1
    return size

answer = 0
sizes = []
m, n, k = map(int, input().split())
graph = [[False] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for _ in range(k):
    sy, sx, ey, ex = map(int, input().split())
    for i in range(sy, ey):
        for j in range(sx, ex):
            graph[i][j] = True

for i in range(n):
    for j in range(m):
        if not visited[i][j] and not graph[i][j]:
            answer += 1
            sizes.append(BFS(i, j))

print(answer)
print(*sorted(sizes))