import sys

input = sys.stdin.readline

def solution():
    def DFS(x, L):
        nonlocal flag
        if flag:
            return
        if L == 5:
            flag = True
        else:
            for nx in graph[x]:
                if not check[nx]:
                    check[nx] = True
                    DFS(nx, L+1)
                    check[nx] = False

    N, M = map(int, input().split())

    flag = False
    graph = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(N):
        check = [False] * N
        check[i] = True
        DFS(i, 1)
        if flag:
            return 1
    return 0

print(solution())