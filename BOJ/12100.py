import sys
from collections import deque
from copy import deepcopy

result = 0
n = int(sys.stdin.readline())
board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

def move(board, dir):
    if dir == 0:    # 위쪽으로 이동
        for i in range(n):
            queue = deque([board[j][i] for j in range(n) if board[j][i] != 0])
            for j in range(n):
                if len(queue) > 1 and queue[0] == queue[1]:
                    board[j][i] = queue.popleft() + queue.popleft()
                else:
                    board[j][i] = queue.popleft() if queue else 0
    elif dir == 1:  # 아래쪽으로 이동
        for i in range(n):
            queue = deque([board[j][i] for j in range(n) if board[j][i] != 0])
            for j in range(n)[::-1]:
                if len(queue) > 1 and queue[-1] == queue[-2]:
                    board[j][i] = queue.pop() + queue.pop()
                else:
                    board[j][i] = queue.pop() if queue else 0
    elif dir == 2:  # 왼쪽으로 이동
        for i in range(n):
            queue = deque([x for x in board[i] if x != 0])
            for j in range(n):
                if len(queue) > 1 and queue[0] == queue[1]:
                    board[i][j] = queue.popleft() + queue.popleft()
                else:
                    board[i][j] = queue.popleft() if queue else 0
    elif dir == 3:  # 오른쪽으로 이동
        for i in range(n):
            queue = deque([x for x in board[i] if x != 0])
            for j in range(n)[::-1]:
                if len(queue) > 1 and queue[-1] == queue[-2]:
                    board[i][j] = queue.pop() + queue.pop()
                else:
                    board[i][j] = queue.pop() if queue else 0
    return board

def DFS(board, L):
    global result
    if L == 5:
        result = max(result, max(map(max, board)))
        print(board)
    else:
        for i in range(4):
            DFS(move(deepcopy(board), i), L + 1)

DFS(board, 0)
print(result)