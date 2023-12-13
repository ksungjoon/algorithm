from collections import defaultdict

def solution(gems):
    answer = []
    n = len(gems)
    min_diff = n
    cnt = len(set(gems))
    dic = defaultdict(int)
    l, r = 0, 0
    dic[gems[l]] += 1
    while r < n:
        if len(dic) >= cnt:
            if min_diff > r - l:
                min_diff = r - l
                answer = [l+1, r+1]
            dic[gems[l]] -= 1
            if dic[gems[l]] == 0:
                del dic[gems[l]]
            l += 1
        else:
            r += 1
            if r == n:
                break
            dic[gems[r]] += 1
    return answer