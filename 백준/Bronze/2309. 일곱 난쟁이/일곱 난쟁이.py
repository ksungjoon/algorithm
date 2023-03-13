lst = [int(input())for i in range(9)]
total = sum(lst)
minus = total-100
flag = 0
a,b=0,0
for i in range(8):
    for j in range(i+1,9):
        if minus==lst[i]+lst[j]:
            a = lst[i]
            b = lst[j]
            lst.remove(a)
            lst.remove(b)
            flag = 1
            break
    if flag ==1:
        break
lst.sort()
for i in range(7):
    print(lst[i])