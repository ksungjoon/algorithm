N = int(input())
lst = [list(map(int,input().split()))for i in range(N)]
white = [[0]*1001 for i in range(1001)]
for i in range(N):
    for j in range(lst[i][0],lst[i][0]+lst[i][2]):
        for k in range(lst[i][1],lst[i][1]+lst[i][3]):
            white[k][j]=i+1
for z in range(1,N+1):
    cnt = 0
    for l in range(1001):
        for m in range(1001):
            if white[l][m]==z:
                cnt+=1
    print(cnt)