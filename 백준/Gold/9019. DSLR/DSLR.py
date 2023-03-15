from collections import deque
import sys

input = sys.stdin.readline


def BFS():
    queue = deque()
    check = [False] * 10001
    check[A] = True
    queue.append((A, ""))
    while queue:
        n, pro = queue.popleft()

        if n == B:
            return pro
        
        # D
        nn = n * 2
        if nn > 9999:
            nn %= 10000
        if not check[nn]:
            check[nn] = True
            queue.append((nn, pro + "D"))

        # S
        nn = n - 1
        if nn < 0:
            nn = 9999
        if not check[nn]:
            check[nn] = True
            queue.append((nn, pro + "S"))

        # L
        nn = ((n % 1000) * 10) + (n // 1000)
        if not check[nn]:
            check[nn] = True
            queue.append((nn, pro + "L"))

        # R
        nn = ((n % 10) * 1000) + (n // 10)
        if not check[nn]:
            check[nn] = True
            queue.append((nn, pro + "R"))


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(BFS())