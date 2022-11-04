from collections import deque
import sys

n = int(sys.stdin.readline())
colored_paper = []
white = 0
blue = 0

for _ in range(n):
    colored_paper.append(list(map(int, sys.stdin.readline().split())))
    
flag = False
for i in range(n-1):
    if colored_paper[i-1] != colored_paper[i]:
        flag = True
        break
        
if not flag:
    if colored_paper[0][0] == 0:
        white = 1
    else:
        blue = 1
else:
    queue = deque()
    queue.append(colored_paper)
    while queue:
        v = queue.popleft()
        vn = len(v) // 2
        for start, end in [[0, vn], [vn, vn*2]]:
            a = []
            b = []
            a_color = v[start][0]
            b_color = v[start][vn]
            a_flag = False
            b_flag = False
            for i in range(start, end):
                a_tmp = []
                for j in range(vn):
                    if not a_flag and v[i][j] != a_color:
                        a_flag = True
                    a_tmp.append(v[i][j])
                a.append(a_tmp)
                b_tmp = []
                for j in range(vn, vn*2):
                    if not b_flag and v[i][j] != b_color:
                        b_flag = True
                    b_tmp.append(v[i][j])
                b.append(b_tmp)
            for flag, color, nv in [['a_flag', 'a_color', 'a'], ['b_flag', 'b_color', 'b']]:
                if eval(flag):
                    queue.append(eval(nv))
                else:
                    if eval(color) == 0:
                        white += 1
                    else:
                        blue += 1
            
print(white)
print(blue)