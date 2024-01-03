from collections import defaultdict
def solution(genres, plays):
    answer = []
    genres_count = defaultdict(int)
    genres_play = defaultdict(list)
    i = 0
    for g, p in zip(genres, plays):
        genres_count[g] += p
        genres_play[g].append((p, i))
        i += 1
    genres_order = sorted(genres_count, key= lambda k: -genres_count[k])
    for g in genres_order:
        temp = genres_play[g]
        temp.sort(key= lambda x: (-x[0], x[1]))
        if len(temp) > 1:
            answer.append(temp[0][1])
            answer.append(temp[1][1])
        else:
            answer.append(temp[0][1])
    return answer