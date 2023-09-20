import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def dijkstra(start):
    heap = []
    distance = [sys.maxsize] * (n+1)
    distance[start] = 0
    heappush(heap, (0, start))
    while heap:
        dist, now = heappop(heap)
        if distance[now] < dist:
            continue
        for next, cost in graph[now]:
            next_dist = dist + cost
            if distance[next] > next_dist:
                distance[next] = next_dist
                heappush(heap, (next_dist, next))
    return distance

answer = 0
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, t = map(int, input().split())
    graph[start].append((end, t))

for i in range(1, n+1):
    answer = max(answer, dijkstra(i)[x] + dijkstra(x)[i])

print(answer)