import sys

input = sys.stdin.readline
INF = sys.maxsize

N, S = map(int, input().split())
nums = list(map(int, input().split()))

answer = INF
total = 0
left = 0
for right in range(N):
    if total < S:
        total += nums[right]
    while total >= S:
        answer = min(answer, right - left + 1)
        total -= nums[left]
        left += 1

print(answer if answer != INF else 0)