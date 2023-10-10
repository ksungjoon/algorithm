def solution(s):
    a = 0
    answer = True
    for i in s:
        if i =='(':
            a+=1
        elif i ==')':
            a-=1
        if a < 0:
            answer= False
            break
    if a!=0:
        answer=False
    return answer