import sys

input = sys.stdin.readline

count = [0] * 26
s = input().rstrip()

for x in s:
    count[ord(x)-ord('a')] += 1

print(*count)