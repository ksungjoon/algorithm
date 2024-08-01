def solution(data, ext, val_ext, sort_by):
    answer = []
    if ext == 'code':
        for i in range(len(data)):
            if data[i][0] < val_ext:
                answer.append(data[i])
    elif ext == 'date':
        for i in range(len(data)):
            if data[i][1] < val_ext:
                answer.append(data[i])
    elif ext == 'maximum':
        for i in range(len(data)):
            if data[i][2] < val_ext:
                answer.append(data[i])
    elif ext == 'remain':
        for i in range(len(data)):
            if data[i][3] < val_ext:
                answer.append(data[i])
    
    if sort_by == 'code':
        answer= sorted(answer, key=lambda x:x[0])
    elif sort_by == 'date':
        answer= sorted(answer, key=lambda x:x[1])
    elif sort_by == 'maximum':
        answer= sorted(answer, key=lambda x:x[2])
    elif sort_by == 'remain':
        answer= sorted(answer, key=lambda x:x[3])
    return answer