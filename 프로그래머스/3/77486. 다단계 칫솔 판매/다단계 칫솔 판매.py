from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    parents_dic = defaultdict(str)
    amount_dic = defaultdict(int)

    for i in range(len(enroll)):
        if referral[i] != '-':
            parents_dic[enroll[i]] = referral[i]

    for i in range(len(seller)):
        parent = seller[i]
        sell = amount[i] * 100
        while parent != "":
            amount_dic[parent] +=  sell-sell//10
            sell = sell//10 
            parent = parents_dic[parent]
            if sell == 0:
                break

    for i in enroll:
        answer.append(amount_dic[i])

    return answer
