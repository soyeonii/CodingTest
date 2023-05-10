import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]


def DFS(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and board[x][y] == board[nx][ny]:
                visited[nx][ny] = True
                DFS(nx, ny)


count = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            DFS(i, j)
            count += 1
print(count, end=" ")

for i in range(N):
    for j in range(N):
        if board[i][j] == "G":
            board[i][j] = "R"

count = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            DFS(i, j)
            count += 1
print(count)