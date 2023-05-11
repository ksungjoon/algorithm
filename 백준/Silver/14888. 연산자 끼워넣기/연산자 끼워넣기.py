N = int(input())
lst = list(map(int,input().split()))
sign_lst = list(map(int,input().split()))
Max = -21e9
Min = 21e9
def dfs(lev,result):
    global Min,Max
    if lev==N-1:
        if result<Min:
            Min=result
        if result>Max:
            Max=result
        return
    for i in range(4):
        if sign_lst[i] != 0:
            sign_lst[i]-=1
            if i == 0:
                dfs(lev + 1, result+lst[lev+1])
            elif i == 1:
                dfs(lev + 1, result-lst[lev+1])
            elif i == 2:
                dfs(lev + 1, result*lst[lev+1])
            elif i == 3:
                if result<0:
                    dfs(lev + 1, -(-result // lst[lev+1]))
                else:
                    dfs(lev + 1, result//lst[lev+1])
            sign_lst[i] += 1


dfs(0,lst[0])
print(Max)
print(Min)
