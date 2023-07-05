import sys

input = sys.stdin.readline

answer = []
n = int(input())
name = []
count = [0] * 26

for _ in range(n):
    name.append(input().rstrip())

for x in name:
    count[ord(x[0])-ord('a')] += 1

for i in range(26):
    if count[i] >= 5:
        answer.append(chr(ord('a')+i))

print("".join(answer) if answer else "PREDAJA")