# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         cnt = 0
#         if i == len(prices)-1:
#             answer.append(0)
#             break
#         for j in range(i+1,len(prices)):
#             cnt+=1
#             if prices[i]>prices[j]:
#                 break
#         answer.append(cnt)
#     return answer

def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            elif prices[i] > prices[j] and i+1 != len(prices):
                cnt += 1
                break
            else:
                break
        answer.append(cnt)
    
    return answer