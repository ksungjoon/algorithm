X = int(input())
N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

lst_sum = 0

for i in range(len(lst)):
    lst_sum += lst[i][0]*lst[i][1]

if lst_sum == X :
    print('Yes')
else:
    print('No')