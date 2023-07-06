import sys
from collections import Counter

input = sys.stdin.readline

def solution():
    answer = ""
    mid = ""
    name = input().rstrip()
    count = Counter(name)

    for k, v in sorted(count.items()):
        if v & 1:
            if mid:
                return "I'm Sorry Hansoo"
            mid = k
        answer += k * (v // 2)

    return answer + mid + answer[::-1]

print(solution())