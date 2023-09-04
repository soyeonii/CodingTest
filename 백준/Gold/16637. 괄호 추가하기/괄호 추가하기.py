import sys

input = sys.stdin.readline

n = int(input())
s = input()
answer = -sys.maxsize

def DFS(i, value):
    global answer
    if i == n - 1:
        answer = max(answer, value)
        return
    if i + 2 < n:
        DFS(i + 2, eval(str(value) + s[i+1:i+3]))
    if i + 4 < n:
        DFS(i + 4, eval(str(value) + s[i+1] + str(eval(s[i+2:i+5]))))

DFS(0, int(s[0]))
print(answer)