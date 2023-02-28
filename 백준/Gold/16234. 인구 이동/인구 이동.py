from collections import deque
import sys
input = sys.stdin.readline


def solution():
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def BFS(i, j):
        nonlocal visited
        queue = deque()
        queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if L <= abs(population[x][y] - population[nx][ny]) <= R:
                        stack.append((nx, ny))
                        visited[nx][ny] = True
                        queue.append((nx, ny))

    def union():
        global population
        avg = sum([population[x][y] for x, y in stack]) // len(stack)
        for x, y in stack:
            population[x][y] = avg

    while True:
        flag = False
        visited = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    stack = []
                    BFS(i, j)
                    if stack:
                        flag = True
                        union()
        if not flag:
            return answer
        answer += 1


N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]
print(solution())