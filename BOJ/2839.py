import sys

def solution(n):
    answer = n // 5
    n %= 5
    while 0 <= answer:
        if n % 3 == 0:
            return answer + n // 3
        answer -= 1
        n += 5
    return -1

print(solution(int(sys.stdin.readline())))