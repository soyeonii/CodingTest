from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline


def solution():
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def count(nboard):
        result = 0
        for i in range(N):
            for j in range(M):
                if nboard[i][j] == 0:
                    result += 1
        return result

    def BFS(i, j, nboard):
        queue = deque()
        queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and nboard[nx][ny] == 0:
                    nboard[nx][ny] = 3
                    queue.append((nx, ny))

    def DFS(L):
        nonlocal answer
        if L == 3:
            nboard = deepcopy(board)
            for i in range(N):
                for j in range(M):
                    if board[i][j] == 2:
                        BFS(i, j, nboard)
            answer = max(answer, count(nboard))
        else:
            for i in range(N):
                for j in range(M):
                    if board[i][j] == 0:
                        board[i][j] = 1
                        DFS(L + 1)
                        board[i][j] = 0

    DFS(0)
    return answer


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
print(solution())