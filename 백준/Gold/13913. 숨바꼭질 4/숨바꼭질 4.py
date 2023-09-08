import sys
from collections import deque

input = sys.stdin.readline

def BFS(start, path):
    queue = deque()
    visited = [False] * 100001
    queue.append((start, path))
    visited[start] = True
    L = 0
    while queue:
        for _ in range(len(queue)):
            x, p = queue.popleft()
            if x == k:
                return L, p
            for nx in [x-1, x+1, x*2]:
                if 0 <= nx <= 100000 and not visited[nx]:
                    queue.append((nx, p + [nx]))
                    visited[nx] = True
        L += 1

n, k = map(int, input().split())

if n > k:
    time = n - k
    path = range(k, n+1)[::-1]
else:
    time, path = BFS(n, [n])
    
print(time)
print(*path)