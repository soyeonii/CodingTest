import sys

input = sys.stdin.readline

def DFS(L, left):
    global answer, check, stack
    if L == k:
        answer.append(''.join(map(str, stack)))
    else:
        for right in range(10):
            if not check[right]:
                if eval(str(left) + sign[L] + str(right)):
                    check[right] = True
                    stack.append(right)
                    DFS(L+1, right)
                    stack.pop()
                    check[right] = False

answer = []
k = int(input())
sign = list(input().split())
check = [False] * 10
stack = []

for i in range(10):
    check[i] = True
    stack.append(i)
    DFS(0, i)
    stack.pop()
    check[i] = False

print(answer[-1])
print(answer[0])