import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS():
    melt = []
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
                    melt.append((nx, ny))
                visited[nx][ny] = True
    for i, j in melt:
        graph[i][j] = 0
    return len(melt)

time = 0
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
cheeze = sum([sum(x) for x in graph])

while True:
    time += 1
    count = BFS()
    cheeze -= count
    if not cheeze:
        print(time, count, sep='\n')
        break