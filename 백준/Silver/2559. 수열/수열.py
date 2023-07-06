import sys

input = sys.stdin.readline

answer = -sys.maxsize
n, k = map(int, input().split())
temperature = list(map(int, input().split()))
psum = [0] * (n + 1)

for i in range(1, n+1):
    psum[i] = psum[i-1] + temperature[i-1]

for i in range(k, n+1):
    answer = max(answer, psum[i] - psum[i-k])

print(answer)