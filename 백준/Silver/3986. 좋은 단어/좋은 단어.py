import sys

input = sys.stdin.readline

count = 0
n = int(input())

for _ in range(n):
    word = input().rstrip()
    stack = []
    for x in word:
        if not stack or stack[-1] != x:
            stack.append(x)
        else:
            stack.pop()
    if not stack:
        count += 1

print(count)