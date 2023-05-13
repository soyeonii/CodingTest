import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


def getStart():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                graph[i][j] = 0
                return (i, j)


def BFS(x, y):
    fish = []
    L = 0
    queue = deque()
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    queue.append((x, y))
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if graph[nx][ny] == 0 or graph[nx][ny] == size:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                    elif graph[nx][ny] < size:
                        visited[nx][ny] = True
                        fish.append((nx, ny))
        L += 1
        if fish:
            fish.sort()
            graph[fish[0][0]][fish[0][1]] = 0
            return [fish[0], L]
    return [[], 0]


time = 0
baby_shark = getStart()
size = 2
eaten = 0

while True:
    baby_shark, t = BFS(baby_shark[0], baby_shark[1])
    if t == 0:
        print(time)
        break
    else:
        time += t
        eaten += 1
        if size == eaten:
            size += 1
            eaten = 0