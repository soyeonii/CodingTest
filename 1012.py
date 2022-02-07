from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    result = 0
    
    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1
                
    print(result)
