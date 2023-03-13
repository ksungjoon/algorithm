sum=0
arr =[[0]*101 for _ in range(101)]
lst =[list(map(int,input().split()))for i in range(4)]
for i in range(4):
    for j in range(lst[i][1],lst[i][3]):
        for k in range(lst[i][0],lst[i][2]):
            arr[j][k]=1
for i in range(101):
    for j in range(101):
        sum += arr[i][j]
print(sum)