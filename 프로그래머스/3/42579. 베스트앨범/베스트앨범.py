def solution(genres, plays):
    result = []
    playlst = {}
    for i in range(len(genres)):
        if genres[i] not in playlst:
            playlst[genres[i]]=[(i,plays[i])]
        else:
            playlst[genres[i]].append((i,plays[i]))

    for idx, songs in playlst.items():
        playlst[idx] = sorted(songs, key=lambda x: x[1], reverse=True)

    sorted_playlst = sorted(playlst.items(), key=lambda x: sum(song[1] for song in x[1]), reverse=True)
    
    for j in sorted_playlst:
        if len(j[1]) >= 2:
            result.append(j[1][0][0])
            result.append(j[1][1][0])
        else:
            result.append(j[1][0][0])
        
    return result