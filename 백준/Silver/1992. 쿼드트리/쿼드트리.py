import sys

input = sys.stdin.readline


def check(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if image[i][j] != image[x][y]:
                return False
    return True


def QuadTree(x, y, n):
    if check(x, y, n):
        print(image[x][y], end="")
    else:
        print("(", end="")
        n //= 2
        QuadTree(x, y, n)
        QuadTree(x, y + n, n)
        QuadTree(x + n, y, n)
        QuadTree(x + n, y + n, n)
        print(")", end="")


N = int(input())
image = [list(input().rstrip()) for _ in range(N)]

QuadTree(0, 0, N)