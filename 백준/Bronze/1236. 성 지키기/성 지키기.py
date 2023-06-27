N,M = map(int,input().split())
castle = [list(map(str,input()))for i in range(N)]
row = 0
col = 0
for i in range(N):
    if 'X' not in castle[i]:
        row+=1

for j in range(M):
    flag = 0
    for i in range(N):
        if castle[i][j]=='X':
            flag=1
            break
    if flag ==0:
        col+=1
if row >= col:
    print(row)
else:
    print(col)