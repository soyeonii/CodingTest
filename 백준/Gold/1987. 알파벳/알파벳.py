import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
check = [False] * 26
answer = 0


def DFS(x, y, L):
    global answer
    answer = max(answer, L)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            idx = ord(board[nx][ny]) - ord("A")
            if not check[idx]:
                check[idx] = True
                DFS(nx, ny, L + 1)
                check[idx] = False


check[ord(board[0][0]) - ord("A")] = True
DFS(0, 0, 1)
print(answer)