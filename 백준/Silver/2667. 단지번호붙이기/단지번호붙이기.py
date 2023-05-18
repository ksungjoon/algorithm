from collections import deque
N = int(input())
lst = [list(map(int,input()))for _ in range(N)]
diry = [-1,0,0,1]
dirx = [0,-1,1,0]
result =[]
def bfs(sty,stx):
    que = deque()
    cnt = 0
    que.append((sty,stx))
    lst[sty][stx]=0
    while que:
        a,b = que.popleft()
        cnt += 1
        for i in range(4):
            dy = diry[i]+a
            dx = dirx[i]+b
            if 0<=dy<N and 0<=dx<N and lst[dy][dx]==1:
                que.append((dy,dx))
                lst[dy][dx]=0
    return cnt
for i in range(N):
    for j in range(N):
        if lst[i][j]==1:
            result.append(bfs(i,j))
result.sort()
print(len(result))
for i in result:
    print(i)
