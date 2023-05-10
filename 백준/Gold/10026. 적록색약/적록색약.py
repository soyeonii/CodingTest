import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
board = [list(input()) for _ in range(N)]
visited1 = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]


def BFS(x, y, color_weakness):
    queue = deque()
    queue.append((x, y, color_weakness))
    while queue:
        x, y, color_weakness = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not color_weakness:
                    if not visited1[nx][ny] and board[x][y] == board[nx][ny]:
                        visited1[nx][ny] = True
                        queue.append((nx, ny, color_weakness))
                else:
                    if not visited2[nx][ny]:
                        if board[x][y] == "B":
                            if board[x][y] == board[nx][ny]:
                                visited2[nx][ny] = True
                                queue.append((nx, ny, color_weakness))
                        else:
                            if board[nx][ny] != "B":
                                visited2[nx][ny] = True
                                queue.append((nx, ny, color_weakness))


count1 = 0
count2 = 0
for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            visited1[i][j] = True
            BFS(i, j, False)
            count1 += 1
        if not visited2[i][j]:
            visited2[i][j] = True
            BFS(i, j, True)
            count2 += 1
print(count1, count2)