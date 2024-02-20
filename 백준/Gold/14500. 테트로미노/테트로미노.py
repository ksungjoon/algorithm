import sys
input = sys.stdin.readline
N,M = map(int,input().split())
lst = [list(map(int,input().split())) for i in range(N)]
Max = -21e9
check_lst = [[0]*M for _ in range(N)]
diret_x = [0,-1,1,0]
diret_y = [-1,0,0,1]
def dfs(sty,stx,lev,Sum):
    global Max
    if lev == 4:
        if Max < Sum:
            Max = Sum
        return
    for i in range(4):
        dy = sty+diret_y[i]
        dx = stx+diret_x[i]
        if 0<=dy<N and 0<=dx<M:
            if check_lst[dy][dx]==0:
                check_lst[dy][dx] = 1
                dfs(dy,dx,lev+1,Sum+lst[dy][dx])
                check_lst[dy][dx] = 0

def exce(i, j):
    global Max
    for n in range(4):

        tmp = lst[i][j]
        for k in range(3):
   
            t = (n+k)%4
            ni = i+diret_y[t]
            nj = j+diret_x[t]

            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += lst[ni][nj]
      
        Max = max(Max, tmp)
for i in range(N):
    for j in range(M):
        dfs(i,j,0,0)
        exce(i,j)
print(Max)