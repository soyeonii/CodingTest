from collections import deque
import sys

input = sys.stdin.readline


def BFS():
    answer = []

    def pour(a, b):
        if not check[a][b]:
            check[a][b] = True
            queue.append((a, b))

    queue = deque()
    check = [[False] * (B + 1) for _ in range(A + 1)]
    check[0][0] = True
    queue.append((0, 0))
    while queue:
        a, b = queue.popleft()
        c = C - (a + b)

        if a == 0:
            answer.append(c)

        # A -> B
        water = min(a, B - b)
        pour(a - water, b + water)
        # A -> C
        water = min(a, C - c)
        pour(a - water, b)
        # B -> A
        water = min(b, A - a)
        pour(a + water, b - water)
        # B -> C
        water = min(b, C - c)
        pour(a, b - water)
        # C -> A
        water = min(c, A - a)
        pour(a + water, b)
        # C -> B
        water = min(c, B - b)
        pour(a, b + water)

    return sorted(answer)


A, B, C = map(int, input().split())
for x in BFS():
    print(x, end=" ")