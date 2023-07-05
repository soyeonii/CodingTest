import sys

input = sys.stdin.readline

answer = ""
s = input().rstrip()
n = len(s)

for i in range(n):
    if s[i].isalpha():
        x = ord(s[i]) + 13
        if s[i].isupper():
            if x > ord("Z"):
                x -= 26
        else:
            if x > ord("z"):
                x -= 26
        answer += chr(x)
    else:
        answer += s[i]

print(answer)