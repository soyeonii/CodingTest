import sys

input = sys.stdin.readline

def solution():
    file_name = input()
    if file_name.startswith(start) and file_name.endswith(end) and len(file_name) >= len(start + end):
        return "DA"
    return "NE"

n = int(input())
start, end = input().split("*")

for _ in range(n):
    print(solution())