def solution(word):
    count = 0
    flag = False
    stack = []
    
    def DFS():
        nonlocal count, flag
        if len(stack) < 5:
            for i in ['A', 'E', 'I', 'O', 'U']:
                if not flag:
                    count += 1
                    stack.append(i)
                    if ''.join(stack) == word:
                        flag = True
                        return
                    DFS()
                    stack.pop()
                    
    DFS()
    return count