from collections import defaultdict

def solution(topping):
    answer = 0
    A = defaultdict(int)
    B = defaultdict(int)
    for i in topping:
        A[i]+=1
    for i in topping:
        B[i]+=1
        A[i]-=1
        if A[i]==0:
            del A[i]
        if len(B)==len(A):
            answer+=1
    return answer