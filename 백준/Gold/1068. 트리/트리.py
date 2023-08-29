import sys

input = sys.stdin.readline

def DFS(start):
    global answer
    if not tree[start]:
        answer += 1
    else:
        for x in tree[start]:
            DFS(x)

answer = 0
n = int(input())
parent_nodes = list(map(int, input().split()))
delete_node = int(input())

tree = [[] for _ in range(n)]
root_node = 0

for i in range(n):
    if parent_nodes[i] == -1:
        root_node = i
    elif i != delete_node and parent_nodes[i] != delete_node:
            tree[parent_nodes[i]].append(i)

if root_node == delete_node:
    print(0)
else:
    DFS(root_node)
    print(answer)