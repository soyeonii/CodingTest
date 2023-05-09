import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

total = 0
remainder = [0] * M
for i in range(N):
    total += A[i]
    remainder[total % M] += 1

answer = remainder[0]
for i in remainder:
    answer += (i * (i-1)) // 2

print(answer)