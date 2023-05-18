from collections import deque

N,K = map(int,input().split())
cnt_lst=[0]*100001
def bfs(st):
    que = deque()
    que.append(st)
    while que:
        a = que.popleft()
        if a == K:
            return cnt_lst[a]
        for i in (a-1,a+1,a*2):
            if 0<= i <= 100000 and not cnt_lst[i]:
                cnt_lst[i]=cnt_lst[a]+1
                que.append(i)
print(bfs(N))