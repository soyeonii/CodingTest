import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(i, j):
    count = 0
    queue = deque()
    visited = [[0] * n for _ in range(m)]
    queue.append((i, j))
    visited[i][j] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 'L':
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    count = max(count, visited[nx][ny])
    return count - 1

answer = 0
m, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m)]

for i in range(m):
    for j in range(n):
        if graph[i][j] == 'L':
            answer = max(answer, BFS(i, j))

print(answer)