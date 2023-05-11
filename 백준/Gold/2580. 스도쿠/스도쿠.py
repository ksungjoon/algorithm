lst = [list(map(int,input().split()))for i in range(9)]
exp=[1,2,3,4,5,6,7,8,9]
empty = [(i,j) for i in range(9) for j in range(9) if lst[i][j]==0]

def result(lst):
    possible = [i for i in exp if i not in lst]
    return possible
def result2(x):
    if 0<=x<=2:
        return [0,1,2]
    elif 3<=x<=5:
        return [3,4,5]
    elif 6<=x<=8:
        return [6,7,8]
def is_possible(y,x):
    possible = result(lst[y])
    sero = [lst[k][x] for k in range(9)]
    possible2 = result(sero)
    s_sero = result2(y)
    s_garo = result2(x)
    s_box = [lst[k][z] for z in s_garo for k in s_sero]
    possible3 = result(s_box)
    possible = [i for i in possible if i in possible3 and i in possible2]
    return possible

flag=0
def dfs(z):
    global flag
    if z == len(empty):
        for i in range(9):
            print(*lst[i])
        flag=1
        return
    tmp = is_possible(empty[z][0],empty[z][1])
    if len(tmp)==0:
        return
    for k in tmp:
        lst[empty[z][0]][empty[z][1]]=k
        dfs(z+1)
        if flag ==1:
            return
        lst[empty[z][0]][empty[z][1]] = 0

dfs(0)