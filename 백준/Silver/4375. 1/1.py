import sys

input = sys.stdin.readline

while True:
    try:
        n = int(input())
    except:
        break
    result = 1
    count = 1
    while True:
        if result % n == 0:
            print(count)
            break
        else:
            result = result * 10 + 1
            result %= n
            count += 1