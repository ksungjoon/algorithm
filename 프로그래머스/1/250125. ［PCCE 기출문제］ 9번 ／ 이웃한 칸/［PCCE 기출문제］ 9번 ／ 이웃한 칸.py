def solution(board, h, w):
    answer = 0
    y_lst=[-1,0,0,1]
    x_lst=[0,-1,1,0]
    for i in range(4):
        by = y_lst[i]+h
        bx = x_lst[i]+w
        if 0<= by <len(board) and  0<= bx <len(board):
            if board[by][bx] == board[h][w]:
                answer +=1
            
    return answer