import sys

input = sys.stdin.readline


def solution():
    for i in range(n-1):
        if phone_num[i+1].startswith(phone_num[i]):
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    phone_num = sorted([input().rstrip() for _ in range(n)])
    print(solution())