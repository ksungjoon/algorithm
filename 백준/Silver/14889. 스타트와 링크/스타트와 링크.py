N = int(input())
lst = [list(map(int,input().split()))for i in range(N)]
member = [i for i in range(N)]
a_team=[0]*(N//2)
Min = 21e9

def score(lsta,lstb):
    a_sum=0
    b_sum=0
    for i in range(len(lsta)-1):
        for j in range(i+1,len(lsta)):
            a_sum+=lst[lsta[i]][lsta[j]]
            a_sum+=lst[lsta[j]][lsta[i]]
            b_sum += lst[lstb[i]][lstb[j]]
            b_sum += lst[lstb[j]][lstb[i]]
    return abs(a_sum-b_sum)

def dfs(lev,start):
    global Min
    if lev==N//2:
        b_team = [i for i in member if i not in a_team]
        result=score(a_team,b_team)
        if Min > result:
            Min = result
        return
    for i in range(start,N):
        a_team[lev]=member[i]
        dfs(lev+1,i+1)
        a_team[lev]=0

dfs(0,0)

print(Min)
