import sys

input = sys.stdin.readline

def isCorrect():
    for i in range(n):
        line = i
        for j in range(h):
            if check[j][line]:
                line += 1
            elif line > 0 and check[j][line-1]:
                line -= 1
        if i != line:
            return False
    return True

def DFS(L, x, y):
    global answer
    if isCorrect():
        answer = min(answer, L)
        return
    if L == 3 or L >= answer:
        return
    for i in range(x, h):
        line = y if i == x else 0
        for j in range(line, n-1):
            if not check[i][j]:
                check[i][j] = True
                DFS(L+1, i, j+2)
                check[i][j] = False

answer = 4
n, m, h = map(int, input().split())
check = [[False] * n for _ in range(h)]

for _ in range(m):
    a, b = map(int, input().split())
    check[a-1][b-1] = True

DFS(0, 0, 0)
print(answer if answer <= 3 else -1)