import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 0, 1, 0]
dz = [0, 0, 0, 1, 0, -1]


def BFS():
    L = -1
    queue = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if boxes[i][j][k] == 1:
                    queue.append((i, j, k))
    while queue:
        for _ in range(len(queue)):
            x, y, z = queue.popleft()
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if (
                    0 <= nx < H
                    and 0 <= ny < N
                    and 0 <= nz < M
                    and boxes[nx][ny][nz] == 0
                ):
                    boxes[nx][ny][nz] = 1
                    queue.append((nx, ny, nz))
        L += 1
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if boxes[i][j][k] == 0:
                    return -1
    return L


print(BFS())