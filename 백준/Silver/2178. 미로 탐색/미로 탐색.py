from collections import deque
N,M = map(int,input().split())
diry=[-1,0,0,1]
dirx=[0,-1,1,0]
lst = [list(map(int,input()))for _ in range(N)]
def bfs(sty,stx):
    que=deque()
    que.append((sty,stx))
    lst[sty][stx]=0
    while que:
        a,b = que.popleft()
        for i in range(4):
            dy = diry[i]+a
            dx = dirx[i]+b
            if 0<=dy<N and 0<=dx<M and lst[dy][dx]==1:
                lst[dy][dx]=lst[a][b]+1
                que.append((dy,dx))
bfs(0,0)

print(lst[N-1][M-1]+1)