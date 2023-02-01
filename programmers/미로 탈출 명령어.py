import sys

sys.setrecursionlimit(100000)

def solution(n, m, x, y, r, c, k):
    lrud = {0: 'd', 1: 'l', 2: 'r', 3: 'u'}
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    answer = 'impossible'
    flag = False
    stack = []

    def DFS(X, Y, L):
        nonlocal answer, flag
        if flag or k < L + abs(X - r) + abs(Y - c):
            return
        if L == k and (X, Y) == (r, c):
            answer = ''.join(stack)
            flag = True
        else:
            for i in range(4):
                nX = X + dx[i]
                nY = Y + dy[i]
                if 1 <= nX <= n and 1 <= nY <= m:
                    stack.append(lrud[i])
                    DFS(nX, nY, L+1)
                    stack.pop()

    dist = abs(x - r) + abs(y - c)
    if dist <= k and (k - dist) % 2 == 0:
        DFS(x, y, 0)
    return answer


print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))
