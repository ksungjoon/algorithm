def process(who, how, answer, parent):
    give = how // 10
    answer[who] += how - give
    if parent[who] == '-':
        return
    if give:
        process(parent[who], give, answer, parent)

def solution(enroll, referral, seller, amount):
    answer = {who: 0 for who in enroll}
    parent = {key: val for key, val in zip(enroll, referral)}

    for who, how in zip(seller, amount):
        process(who, how * 100, answer, parent)

    return list(answer.values())