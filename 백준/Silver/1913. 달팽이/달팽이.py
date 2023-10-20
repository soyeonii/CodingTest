import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
target = int(input())

result = [[0] * n for _ in range(n)]
x = y = n//2
num = 1
move = 1
answer = [x+1, y+1]
result[x][y] = num

while num <= n**2:
    for i in range(2):
        for _ in range(move):
            num += 1
            x = x + dx[i]
            y = y + dy[i]
            if 0 <= x < n and 0 <= y < n:
                result[x][y] = num
                if num == target:
                    answer = [x+1, y+1]
    move += 1
    for i in range(2, 4):
        for _ in range(move):
            num += 1
            x = x + dx[i]
            y = y + dy[i]
            if 0 <= x < n and 0 <= y < n:
                result[x][y] = num
                if num == target:
                    answer = [x+1, y+1]
    move += 1

for x in result:
    print(*x)
print(*answer)