import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS():
    count = 0
    melt = [[False] * n for _ in range(m)]
    queue = deque()
    visited = [[False] * n for _ in range(m)]
    queue.append((0, 0))
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                else:
                    melt[nx][ny] = True
                    count += 1
                visited[nx][ny] = True
    for i in range(m):
        for j in range(n):
            if melt[i][j]:
                graph[i][j] = 0
    return count

time = 0
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
cheeze = sum([sum(x) for x in graph])

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            time += 1
            count = BFS()
            cheeze -= count
            if not cheeze:
                print(time, count, sep='\n')
                sys.exit(0)