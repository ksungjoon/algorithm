N = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))
now=price[0]
result =0
for i in range(len(price)-1):
    if now>price[i+1]:
        result+=now*distance[i]
        now=price[i+1]
    else:
        result+=now*distance[i]
print(result)