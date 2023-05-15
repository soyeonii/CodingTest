import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    n1, n2, w = map(int, input().split())
    graph[n1].append((n2, w))
    graph[n2].append((n1, w))


def DFS(x, w):
    for nx, nw in graph[x]:
        if distance[nx] == -1:
            distance[nx] = w + nw
            DFS(nx, distance[nx])


distance = [-1] * (n + 1)
distance[1] = 0
DFS(1, 0)

start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
DFS(start, 0)

print(max(distance))