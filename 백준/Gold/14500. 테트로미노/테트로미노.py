import sys

input = sys.stdin.readline

dx = [0, 1, 0]
dy = [1, 0, -1]

answer = 0
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


def DFS(x, y, total, L):
    global answer
    if L == 3:
        answer = max(answer, total)
    else:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if L == 1:
                    visited[nx][ny] = True
                    DFS(x, y, total + board[nx][ny], L + 1)
                    visited[nx][ny] = False
                visited[nx][ny] = True
                DFS(nx, ny, total + board[nx][ny], L + 1)
                visited[nx][ny] = False


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i, j, board[i][j], 0)
        visited[i][j] = False

print(answer)