import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS_fire():
    while queue_fire:
        x, y = queue_fire.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if not visited_fire[nx][ny] and graph[nx][ny] != '#':
                    queue_fire.append((nx, ny))
                    visited_fire[nx][ny] = visited_fire[x][y] + 1

def BFS_jihun():
    while queue_jihun:
        x, y = queue_jihun.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if not visited_jihun[nx][ny] and graph[nx][ny] != '#':
                    if not visited_fire[nx][ny] or visited_jihun[x][y] + 1 < visited_fire[nx][ny]:
                        queue_jihun.append((nx, ny))
                        visited_jihun[nx][ny] = visited_jihun[x][y] + 1
            else:
                return visited_jihun[x][y]
    return "IMPOSSIBLE"

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
queue_fire = deque()
queue_jihun = deque()
visited_fire = [[0] * c for _ in range(r)]
visited_jihun = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            queue_jihun.append((i, j))
            visited_jihun[i][j] = 1
        elif graph[i][j] == 'F':
            queue_fire.append((i, j))
            visited_fire[i][j] = 1

BFS_fire()
print(BFS_jihun())