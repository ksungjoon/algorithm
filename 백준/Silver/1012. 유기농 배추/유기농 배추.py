T = int(input())
for test_case in range(T):
    M,N,K = map(int,input().split())
    arr =[[0]*M for _ in range(N)]
    for _ in range(K):
        x,y =map(int,input().split())
        arr[y][x]=1
    diry = [-1,0,0,1]
    dirx = [0,-1,1,0]
    cnt = 0
    def find (y,x):
        global arr
        que = [(y,x)]
        arr[y][x] = 0
        while que:
            y,x = que.pop(0)
            for i in range(4):
                dy = diry[i]+y
                dx = dirx[i]+x
                if 0<=dy<N and 0<=dx<M:
                    if arr[dy][dx]==1:
                        que.append((dy,dx))
                        arr[dy][dx]=0

    for i in range(M):
        for j in range(N):
            if arr[j][i]==1:
                find(j,i)
                cnt+=1
    print(cnt)

