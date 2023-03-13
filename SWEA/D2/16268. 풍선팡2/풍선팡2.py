T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    lst = [list(map(int,input().split()))for i in range(N)]
    diry = [0,-1,0,0,1]
    dirx = [0,0,-1,1,0]
    Max = -21e9
    for i in range(N):
        for j in range(M):
            result = 0
            for k in range(5):
                dy = i+diry[k]
                dx = j+dirx[k]
                if 0<=dy<N and 0<=dx<M:
                    result+=lst[dy][dx]
            Max=max(Max,result)
    print(f'#{test_case} {Max}')

