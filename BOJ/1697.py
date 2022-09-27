from collections import deque
import math

def bfs():
    queue = deque()
    queue.append((n, 0))
    graph[n] = 0  
    while queue:
        v, t = queue.popleft()
        for i in [v-1, v+1, v*2]:
            if 0 <= i <= 100000:
                if graph[i] > t + 1:
                    queue.append((i, t+1))
                    graph[i] = t + 1
        
n, k = map(int, input().split())
graph = [math.inf] * 100001

bfs()

print(graph[k])
