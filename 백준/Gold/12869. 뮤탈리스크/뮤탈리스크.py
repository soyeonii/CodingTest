import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

def BFS(start):
    queue = deque()
    visited = [[[False] * 61 for _ in range(61)] for _ in range(61)]
    queue.append(start)
    L = 0
    while queue:
        for _ in range(len(queue)):
            x = queue.popleft()
            if sum(x) == 0:
                return L
            for i in range(len(attack)):
                nx = [0] * 3
                for j in range(n):
                    nx[j] = max(0, x[j] - attack[i][j])
                if not visited[nx[0]][nx[1]][nx[2]]:
                    queue.append(nx)
                    visited[nx[0]][nx[1]][nx[2]] = True
        L += 1

n = int(input())
scv = list(map(int, input().split()))
attack = list(permutations([9, 3, 1], 3))

print(BFS(scv))