from collections import defaultdict

def solution(genres, plays):
    genres_count = defaultdict(int)
    genres_list = defaultdict(list)
    answer = []
    for i in range(len(genres)):
        genres_count[genres[i]]+=plays[i]
        genres_list[genres[i]].append((i,plays[i]))
    genres_count=sorted(genres_count,key=lambda x:genres_count[x],reverse=True)
    
    for genre,play in genres_list.items():
        genres_list[genre] = sorted(play,key=lambda x:x[1],reverse=True)
    
    for k in genres_count:
        if len(genres_list[k])>1:
            answer.append(genres_list[k][0][0])
            answer.append(genres_list[k][1][0])
        else:
            answer.append(genres_list[k][0][0])
    return answer