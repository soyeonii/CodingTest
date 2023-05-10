import sys

input = sys.stdin.readline

tetrominos = [
    [[(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)]],
    [[(0, 1), (1, 0), (1, 1)]],
    [
        [(1, 0), (2, 0), (2, 1)],
        [(0, 1), (0, 2), (1, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(-1, 2), (0, 1), (0, 2)],
        [(-2, 1), (-1, 1), (0, 1)],
        [(1, 0), (1, 1), (1, 2)],
        [(0, 1), (1, 0), (2, 0)],
        [(0, 1), (0, 2), (1, 2)],
    ],
    [
        [(1, 0), (1, 1), (2, 1)],
        [(-1, 1), (-1, 2), (0, 1)],
        [(-1, 1), (0, 1), (1, 0)],
        [(0, 1), (1, 1), (1, 2)],
    ],
    [
        [(0, 1), (0, 2), (1, 1)],
        [(-1, 1), (0, 1), (1, 1)],
        [(-1, 1), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (2, 0)],
    ],
]

answer = 0
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

for tetromino in tetrominos:
    for t in tetromino:
        for x in range(N):
            for y in range(M):
                if (
                    0 <= x + t[0][0]
                    and x + t[-1][0] < N
                    and 0 <= y + sorted(t, key=lambda x: x[1])[0][1]
                    and y + sorted(t, key=lambda x: x[1])[-1][1] < M
                ):
                    total = board[x][y]
                    for dx, dy in t:
                        nx = x + dx
                        ny = y + dy
                        total += board[nx][ny]
                    answer = max(answer, total)

print(answer)