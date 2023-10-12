def solution(s):
    answer = 0
    num =['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in num:
        if i in s:
            idx = str(num.index(i))
            s = s.replace(i,idx)
    answer = int(s)
    return answer

