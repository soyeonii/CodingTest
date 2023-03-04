from collections import deque
import sys

input = sys.stdin.readline


def BFS():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue = deque()
    count = {}
    count[start] = 0
    queue.append(start)
    while queue:
        board = queue.popleft()

        if board == "123456780":
            return count[board]

        pos = board.find('0')
        x = pos // 3
        y = pos % 3
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                npos = nx * 3 + ny
                nboard = list(board)
                nboard[pos], nboard[npos] = nboard[npos], nboard[pos]
                nboard = "".join(nboard)
                if not count.get(nboard):
                    count[nboard] = count[board] + 1
                    queue.append(nboard)
    return -1


start = ""
for _ in range(3):
    start += "".join(input().split())
print(BFS())