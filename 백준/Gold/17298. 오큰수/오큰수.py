import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
stack = []
answer = [-1] * n

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        answer[stack.pop()] = a[i]
    stack.append(i)

print(*answer)