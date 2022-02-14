from collections import deque
import sys

def bfs():
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
        
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

m, n = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    
bfs()
        
for i in graph:
    if 0 in i:
        print(-1)
        sys.exit()
print(max(map(max, graph)) - 1)
