import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N,M,R = map(int,input().split())
lst = [[]for i in range(N+1)]
cnt = 1
visited=[0]*(N+1)
for i in range(M):
    a,b=map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)
for j in lst:
    j.sort(reverse=True)

def dfs (st):
    global cnt
    visited[st]=cnt
    for i in lst[st]:
        if visited[i] == 0:
            cnt+=1
            dfs(i)
dfs(R)
for i in range(1,N+1):
    print(visited[i])
