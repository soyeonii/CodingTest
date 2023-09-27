import sys

input = sys.stdin.readline

n = int(input())
mp, mf, ms, mv = map(int, input().split())
nutrient = [list(map(int, input().split())) for _ in range(n)]
ret_cost = sys.maxsize
ret_stack = []

for i in range(1, 1 << n):
    stack = []
    p = f = s = v = cost = 0
    for j in range(n):
        if i & (1 << j):
            stack.append(j+1)
            p += nutrient[j][0]
            f += nutrient[j][1]
            s += nutrient[j][2]
            v += nutrient[j][3]
            cost += nutrient[j][4]
            if mp <= p and mf <= f and ms <= s and mv <= v:
                if cost < ret_cost:
                    ret_cost = cost
                    ret_stack = stack
                elif cost == ret_cost:
                    ret_stack = sorted([ret_stack, stack])[0]

if ret_cost == sys.maxsize:
    print(-1)
else:
    print(ret_cost)
    print(*ret_stack)