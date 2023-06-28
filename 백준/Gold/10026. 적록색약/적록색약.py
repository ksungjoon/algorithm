from collections import deque
N = int(input())
lst = [list(map(str,input()))for i in range(N)]
nomalcheck_lst = [[0]*N for _ in range(N)]
abnomalcheck_lst = [[0]*N for _ in range(N)]
diry=[-1,0,0,1]
dirx=[0,-1,1,0]
nomalcnt=0
abnomalcnt=0
def bfs_nomal(sy,sx):
    global nomalcnt
    que = deque()
    que.append((sy,sx))
    while que:
        y,x = que.popleft()
        for i in range(4):
            dy = diry[i]+y
            dx = dirx[i]+x
            if 0<=dy<N and 0<=dx<N:
                if nomalcheck_lst[dy][dx]==0 and lst[sy][sx]==lst[dy][dx]:
                    nomalcheck_lst[dy][dx]=1
                    que.append((dy,dx))
    nomalcnt+=1
def bfs_abnomal(sy,sx):
    global abnomalcnt
    que = deque()
    que.append((sy,sx))
    while que:
        y,x = que.popleft()
        for i in range(4):
            dy = diry[i]+y
            dx = dirx[i]+x
            if 0<=dy<N and 0<=dx<N:
                if abnomalcheck_lst[dy][dx]==0:
                    if lst[sy][sx]=='R' and (lst[dy][dx]=='R'or lst[dy][dx]=='G'):
                        abnomalcheck_lst[dy][dx]=1
                        que.append((dy,dx))
                    if lst[sy][sx]=='G' and (lst[dy][dx]=='R'or lst[dy][dx]=='G'):
                        abnomalcheck_lst[dy][dx] = 1
                        que.append((dy,dx))
                    if lst[sy][sx]=='B' and lst[dy][dx]=='B':
                        abnomalcheck_lst[dy][dx] = 1
                        que.append((dy,dx))
    abnomalcnt+=1

for i in range(N):
    for j in range(N):
        if nomalcheck_lst[i][j]==0:
            bfs_nomal(i,j)
        if abnomalcheck_lst[i][j]==0:
            bfs_abnomal(i,j)
print(nomalcnt,abnomalcnt)