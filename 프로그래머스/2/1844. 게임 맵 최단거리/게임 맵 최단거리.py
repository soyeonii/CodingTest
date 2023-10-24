from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    queue = deque()
    visited = [[False] * col for _ in range(row)]
    queue.append((0, 0))
    visited[0][0] = True
    L = 0
    while queue:
        L += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            if r == row-1 and c == col-1:
                return L
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < row and 0 <= nc < col and maps[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        
    return -1