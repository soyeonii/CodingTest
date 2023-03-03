import sys

input = sys.stdin.readline


def solution(x, y, d):
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = [[False] * M for _ in range(N)]

    while True:
        if not visited[x][y]:
            visited[x][y] = True
            answer += 1
        flag = False
        for i in range(d + 3, d - 1, -1):
            nd = i % 4
            nx = x + dx[nd]
            ny = y + dy[nd]
            if board[nx][ny] == 0 and not visited[nx][ny]:
                flag = True
                x = nx
                y = ny
                d = nd
                break
        if not flag:
            x -= dx[d]
            y -= dy[d]
            if board[x][y] == 1:
                return answer


N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
print(solution(r, c, d))