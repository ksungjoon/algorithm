import copy
N,M = map(int,input().split())
K = int(input())
lst = [list(map(int,input().split()))for i in range(K)]
a,b = map(int,input().split())
new_lst = copy.deepcopy(lst)+[[a,b]]
min_sum = 0
for i in range(K+1):
    if new_lst[i][0] == 1:
        new_lst[i][0] = 0
    elif new_lst[i][0] == 2:
        new_lst[i][0] = M
    elif new_lst[i][0] == 3:
        new_lst[i][0] = new_lst[i][1]
        new_lst[i][1] = 0
    elif new_lst[i][0] == 4:
        new_lst[i][0] = new_lst[i][1]
        new_lst[i][1] = N
for i in range(K):
    if (a==1 and lst[i][0]==2) or (a==2 and lst[i][0]==1):
        min_sum += M
        if lst[i][1]+b>2*N-(lst[i][1]+b):
            min_sum+=(2*N-(lst[i][1]+b))
        else:
            min_sum+=(lst[i][1]+b)
    elif (a ==3 and lst[i][0]==4) or (a==4and lst[i][0]==3):
        min_sum += N
        if lst[i][1]+b>2*M-(lst[i][1]+b):
            min_sum+=(2*M-(lst[i][1]+b))
        else:
            min_sum+=(lst[i][1]+b)
    else:
        min_sum+=(abs(new_lst[-1][0]-new_lst[i][0]))
        min_sum+=(abs(new_lst[-1][1]-new_lst[i][1]))
print(min_sum)


