import sys

input = sys.stdin.readline

total = 0
fee = [0] + list(map(int, input().split()))
time = []
count = [0] * 101

for _ in range(3):
    time.append(list(map(int, input().split())))

for sT, eT in time:
    for i in range(sT, eT):
        count[i] += 1

for i in range(101):
    total += fee[count[i]] * count[i]

print(total)