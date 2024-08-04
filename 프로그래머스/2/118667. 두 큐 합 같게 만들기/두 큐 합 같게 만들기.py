def solution(queue1, queue2):
    answer = 0
    target = (sum(queue1)+sum(queue2)) / 2
    queue = queue1 + queue2 
    now = sum(queue1)
    l,r = 0, len(queue1)
    while l < r < len(queue):
        if now == target:
            return answer
        elif now > target:
            now -= queue[l]
            l += 1
            answer += 1
        else:
            now += queue[r]
            answer+= 1
            r += 1
    return -1