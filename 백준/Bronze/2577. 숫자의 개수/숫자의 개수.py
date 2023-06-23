A=int(input())
B=int(input())
C=int(input())
result = str(A*B*C)
cnt_lst = [0]*10
for i in range(len(result)):
    cnt_lst[int(result[i])]+=1
for j in range(10):
    print(cnt_lst[j])
