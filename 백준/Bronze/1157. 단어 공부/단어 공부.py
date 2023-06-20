word = input()
word_cnt = [0]*26
max_result = 0
result = ''
for i in word:
    word_cnt[ord(i.upper())-65]+=1

for j in range(26):
    if max_result < word_cnt[j]:
        max_result = word_cnt[j]
        result = chr(j+65)
    elif max_result == word_cnt[j]:
        result = '?'
print(result)