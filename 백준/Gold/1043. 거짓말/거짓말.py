import sys

input = sys.stdin.readline
n, m = map(int, input().split())  
know_truth = set(map(int, input().split()[1:])) 
party = [set(map(int, input().split()[1:])) for _ in range(m)] 

for _ in range(m):
    for p in party: 
        if p & know_truth:  
            know_truth |= p  

cnt = 0
for p in party:
    if not p & know_truth:  
        cnt += 1
print(cnt)