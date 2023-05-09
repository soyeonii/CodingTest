import sys

input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
board = [list(input().split()) for _ in range(N)]

home = []
chicken = []
for i in range(N):
    for j in range(N):
        if board[i][j] == "1":
            home.append((i, j))
        elif board[i][j] == "2":
            chicken.append((i, j))

answer = INF
n = len(chicken)
stack = []
check = [False] * n


def DFS(start):
    global answer
    if len(stack) == M:
        total = 0
        for r1, c1 in home:
            dist = []
            for r2, c2 in stack:
                dist.append(abs(r1 - r2) + abs(c1 - c2))
            total += min(dist)
        answer = min(answer, total)
    else:
        for i in range(start, n):
            if not check[i]:
                check[i] = True
                stack.append(chicken[i])
                DFS(i + 1)
                stack.pop()
                check[i] = False


DFS(0)
print(answer)