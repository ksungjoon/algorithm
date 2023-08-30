def solution(s):
    Max = -21e9
    Min = 21e9
    a = list(s.split(' '))
    for i in a:
        if int(i)>Max:
            Max = int(i)
        if int(i)<Min:
            Min = int(i)
    answer = str(Min)+' '+str(Max)
    
    return answer