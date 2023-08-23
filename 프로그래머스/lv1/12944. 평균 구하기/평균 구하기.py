def solution(arr):
    answer = 0
    Sum = 0
    for i in arr:
        Sum+=i
    answer = Sum/len(arr)
    return answer