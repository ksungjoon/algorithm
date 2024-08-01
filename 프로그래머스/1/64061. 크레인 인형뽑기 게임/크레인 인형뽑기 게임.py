def solution(board, moves):
    answer = 0
    bucket = [0]
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if bucket[-1] == board[j][i-1]:
                    answer += 2
                    bucket.pop()
                    board[j][i-1] = 0
                    break
                else:
                    bucket.append(board[j][i-1])
                    board[j][i-1] = 0
                    break
                
    return answer