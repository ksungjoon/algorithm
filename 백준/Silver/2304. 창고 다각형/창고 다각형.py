n= int(input())
lst = [list(map(int,input().split()))for i in range(n)]
changgo=[0]*1001
for i in range(n):
    changgo[lst[i][0]]=lst[i][1]
Max= max(changgo)
lev=0
max1=0
max2=0
sum = 0

for i in range(1001):
    if changgo[i]==Max:
        max1=i
        break
    if lev<changgo[i]:
        lev = changgo[i]
    sum+=lev
lev=0
for i in range(1000,-1,-1):
    if changgo[i]==Max:
        max2=i
        break
    if lev<changgo[i]:
        lev = changgo[i]
    sum+=lev
sum+=(max2-max1+1)*Max
print(sum)

