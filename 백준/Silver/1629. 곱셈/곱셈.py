import sys

input = sys.stdin.readline

def go(a, b):
    if b == 1:
        return a % c
    answer = go(a, b // 2)
    answer = (answer ** 2) % c
    if b & 1:
        answer = (answer * a) % c
    return answer

a, b, c = map(int, input().split())

print(go(a, b))