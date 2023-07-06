import sys

input = sys.stdin.readline

count = 0
n = int(input())
m = int(input())
nums = sorted(list(map(int, input().split())))
left = 0
right = n - 1

while left < right:
    x = nums[left] + nums[right]
    if x < m:
        left += 1
    elif x > m:
        right -= 1
    else:
        count += 1
        left += 1
        right -= 1

print(count)