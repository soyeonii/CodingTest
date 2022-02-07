from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] += graph[x][y]
                    queue.append((nx, ny))
                    
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))
    
bfs(0, 0)
    
print(graph[n-1][m-1])
