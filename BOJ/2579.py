n = int(input())
stairs = []
d = [0] * n

for _ in range(n):
    stairs.append(int(input()))
    
d[0] = stairs[0]
if n > 1:
    d[1] = stairs[0] + stairs[1]
    for i in range(2, n):
        d[i] = max(d[i-2], d[i-3] + stairs[i-1]) + stairs[i]
    
print(d[n-1])
