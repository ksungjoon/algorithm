def solution(book_time):
    answer = 0
    book_time = sorted(book_time,key=lambda x:x[0])
    room=[[book_time[0][1]]]
    for i in range(1,len(book_time)):
        flag = 0
        for k in room:
            if (int(k[-1][0:2])*60) + int(k[-1][3:5])+10 <= (int(book_time[i][0][0:2])*60)+int(book_time[i][0][3:5]):
                k.append(book_time[i][1])
                flag=1
                break
        if flag == 0 :
            room.append([book_time[i][1]])
    answer = len(room)
    return answer