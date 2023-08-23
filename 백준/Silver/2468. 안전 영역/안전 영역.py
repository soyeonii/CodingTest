import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(i, j, height):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > height:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

answer = 1
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for height in range(1, 101):
    count = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > height:
                BFS(i, j, height)
                count += 1
    answer = max(answer, count)

print(answer)