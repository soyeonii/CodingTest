import sys

def w(a, b, c):
    # 종료 조건
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
        
    # 이미 계산한 적이 있는 값인 경우
    if d[a][b][c] != 0:
        return d[a][b][c]
    
    if a < b and b < c:
        d[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        d[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        
    return d[a][b][c]
        
d = [[[0] * 21 for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, sys.stdin.readline().split())    
    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
