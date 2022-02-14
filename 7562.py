from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        if x == end_x and y == end_y:
            print(graph[x][y])
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
        
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
        
t = int(input())

for _ in range(t):
    l = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    graph = [[0] * l for _ in range(l)]
    
    bfs(start_x, start_y)
