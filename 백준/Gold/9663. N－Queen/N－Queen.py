n=int(input())
dat=[0]*n
rup=[0]*n*2
rdown=[0]*n*2
cnt=0

def abc(level):
    global cnt;
    if level==n:
        cnt+=1
        return
    for i in range(n):
        if dat[i]==1: continue
        if rup[level+i]==1: continue
        if rdown[(level-i)+n-1]==1: continue
        rup[level + i] = 1
        rdown[(level - i) + n - 1]=1
        dat[i]=1
        abc(level+1)
        dat[i]=0
        rup[level+i]=0
        rdown[(level - i) + n - 1]=0

abc(0)
print(cnt)