from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    result = 0
    while queue:   
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                result += 1               
    return result
    
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
print(bfs(1))
