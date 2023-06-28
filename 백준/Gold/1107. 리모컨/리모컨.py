import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
useless_buttons = list(input().strip())
result = abs(n - 100)

def is_exist(num):
    nums = list(str(num))
    for n in nums:
        if n in useless_buttons:
            return False
    return True

for i in range(1000001):
    if is_exist(i):
        result = min(result, len(str(i)) + abs(i - n))

print(result)