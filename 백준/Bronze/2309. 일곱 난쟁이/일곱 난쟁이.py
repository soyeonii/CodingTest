import sys

input = sys.stdin.readline

def solution():
    total = 0
    height = []

    for _ in range(9):
        x = int(input())
        total += x
        height.append(x)
    height.sort()

    total -= 100

    for i in range(9):
        for j in range(i+1, 9):
            if height[i] + height[j] == total:
                return [height[k] for k in range(9) if k != i and k != j]
    
for x in solution():
    print(x)