import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    clothes = defaultdict(lambda: 1)
    for _ in range(n):
        clothes[input().rstrip().split()[1]] += 1
    answer = 1
    for x in clothes.values():
        answer *= x
    print(answer - 1)