def solution(board, moves):
    answer = 0
    n = len(board)
    basket = []
    
    for move in moves:
        for i in range(n):
            if board[i][move-1] != 0:
                doll = board[i][move-1]
                if basket and doll == basket[-1]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(board[i][move-1])
                board[i][move-1] = 0
                break
                
    return answer