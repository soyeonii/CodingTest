t = int(input())
d = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90

def p(n):
    if d[n] != 0:
        return d[n]
    d[n] = p(n - 1) + p(n - 5)
    return d[n]   

for _ in range(t):
    n = int(input())
    print(p(n))
