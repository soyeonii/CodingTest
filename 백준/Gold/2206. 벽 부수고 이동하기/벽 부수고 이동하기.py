import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(N)]


def BFS():
    queue = deque()
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][False] = 1
    queue.append((0, 0, False))
    while queue:
        x, y, c = queue.popleft()
        if (x, y) == (N - 1, M - 1):
            return visited[x][y][c]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and not visited[nx][ny][c]:
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    queue.append((nx, ny, c))
                elif board[nx][ny] == 1 and not c:
                    visited[nx][ny][True] = visited[x][y][c] + 1
                    queue.append((nx, ny, True))
    return -1


print(BFS())