from collections import deque

def solution(n, wires):
    answer = n - 2
    
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    rank = [1] * (n+1)
    
    for i, j in wires:
        graph[i].append(j)
        graph[j].append(i)
        indegree[i] += 1
        indegree[j] += 1
    
    def topology_sort():
        nonlocal answer
        queue = deque()
        for i in range(1, n+1):
            if indegree[i] == 1:
                queue.append(i)
                
        while queue:
            x = queue.popleft()
            answer = min(answer, abs(n - rank[x]*2))
            
            for nx in graph[x]:
                indegree[nx] -= 1
                if indegree[nx] == 1:
                    queue.append(nx)
                rank[nx] += rank[x]
                
    topology_sort()
    return answer