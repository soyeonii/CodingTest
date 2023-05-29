import sys

input = sys.stdin.readline


def check(x, y, size):
    color = graph[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if graph[i][j] != color:
                return -1
    return color


def solution(x, y, size):
    global answer
    color = check(x, y, size)
    if color == -1:
        answer += "("
        size //= 2
        solution(x, y, size)
        solution(x, y + size, size)
        solution(x + size, y, size)
        solution(x + size, y + size, size)
        answer += ")"
    else:
        answer += color


N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
answer = ""

solution(0, 0, N)

print(answer)