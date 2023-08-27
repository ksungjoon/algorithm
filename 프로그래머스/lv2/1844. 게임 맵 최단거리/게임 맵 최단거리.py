from collections import deque

def solution(maps):
    answer = 0
    y_lenth = len(maps)
    x_lenth = len(maps[0])
    answer = bfs(y_lenth,x_lenth,maps)
    return answer



def bfs(n,m,maps):
    diry=[-1,0,0,1]
    dirx=[0,-1,1,0]
    used = [[0]*m for _ in range(n)]
    used[0][0]=1
    q = deque()
    q.append([0,0,1])
    while q:
        now = q.popleft()
        y = now[0]
        x = now[1]
        cnt = now[2]
        if y == n-1 and x == m-1:
            return cnt
        for i in range(4):
            dy = y+diry[i]
            dx = x+dirx[i]
            if 0<=dy<n and 0<=dx<m:
                if used[dy][dx]==0 and maps[dy][dx]==1:
                    used[dy][dx]=1
                    q.append([dy,dx,cnt+1])
    return -1