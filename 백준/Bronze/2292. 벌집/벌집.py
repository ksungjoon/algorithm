N = int(input())
cnt = 1
st = 0
while N-1>0:
    if N-st>0:
        st+=1
    N -= st*6
    cnt+=1
print(cnt)