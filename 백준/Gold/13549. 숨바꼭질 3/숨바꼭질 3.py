from collections import deque
import sys

input = sys.stdin.readline


def BFS():
    queue = deque()
    visited = [False] * 100001
    visited[N] = True
    queue.append((N, 0))
    while queue:
        x, t = queue.popleft()
        if x == K:
            return t
        if 0 <= (2 * x) <= 100000 and not visited[2 * x]:
            visited[2 * x] = True
            queue.appendleft((2 * x, t))
        if 0 <= (x - 1) <= 100000 and not visited[x - 1]:
            visited[x - 1] = True
            queue.append((x - 1, t + 1))
        if 0 <= (x + 1) <= 100000 and not visited[x + 1]:
            visited[x + 1] = True
            queue.append((x + 1, t + 1))


N, K = map(int, input().split())
print(BFS())