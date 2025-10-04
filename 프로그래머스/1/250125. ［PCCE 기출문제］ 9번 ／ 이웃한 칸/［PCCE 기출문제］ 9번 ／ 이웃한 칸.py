def solution(board, h, w):
    n = len(board)
    move = [-1, -1, 1, 1]
    
    answer = 0
    for i, m in enumerate(move):
        if i % 2 == 0 and (h+m >= 0 and h+m < n):
            if board[h][w] == board[h+m][w]:
                answer += 1
        elif i % 2 != 0 and (w+m >= 0 and w+m < n):
            if board[h][w] == board[h][w+m]:
                answer += 1
                
    return answer