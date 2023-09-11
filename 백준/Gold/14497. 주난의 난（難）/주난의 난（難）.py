import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS():
    global graph
    check = [[False] * m for _ in range(n)]
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    visited[x1-1][y1-1] = True
    queue.append((x1-1, y1-1))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == x2-1 and ny == y2-1:
                return False
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == '0':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif graph[nx][ny] == '1':
                    check[nx][ny] = True
    for i in range(n):
        for j in range(m):
            if check[i][j]:
                graph[i][j] = '0'
    return True

count = 1
n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

while BFS():
    count += 1

print(count)