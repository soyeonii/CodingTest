import sys
from collections import deque

input = sys.stdin.readline

def BFS(start):
    count = 0
    queue = deque()
    visited = [False] * 100001
    queue.append(start)
    L = 0
    while queue:
        for _ in range(len(queue)):
            x = queue.popleft()
            visited[x] = True
            for nx in [x-1, x+1, x*2]:
                if 0 <= nx <= 100000 and not visited[nx]:
                    if nx == k:
                        count += 1
                    else:
                        queue.append(nx)
        L += 1
        if count:
            return [L, count]

n, k = map(int, input().split())

if n == k:
    print(*[0, 1], sep='\n')
else:
    print(*BFS(n), sep='\n')