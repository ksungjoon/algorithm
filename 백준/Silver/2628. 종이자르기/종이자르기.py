garo,sero=map(int,input().split())
n = int(input())
lst = [list(map(int,input().split()))for i in range(n)]
garo_lst = [0,sero]
sero_lst = [0,garo]
garo_length=[]
sero_length=[]
result = []
for i in range(n):
    if lst[i][0]==1:
        sero_lst.append(lst[i][1])
    else:
        garo_lst.append(lst[i][1])
garo_lst.sort()
sero_lst.sort()
for i in range(1,len(garo_lst)):
    garo_length.append(garo_lst[i]-garo_lst[i-1])
for i in range(1,len(sero_lst)):
    sero_length.append((sero_lst[i]-sero_lst[i-1]))
for i in sero_length:
    for j in garo_length:
        result.append(i*j)
print(max(result))