def solution(wallpaper):
    lux = 100
    luy = 100
    rdx = 0
    rdy = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if luy > i:
                    luy = i
                if lux > j:
                    lux = j
                if rdy < i:
                    rdy = i
                if rdx < j:
                    rdx = j
    answer = [luy,lux,rdy+1,rdx+1]
    return answer