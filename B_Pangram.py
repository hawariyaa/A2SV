n = input()
word = input().strip()
word = word.lower()
alphabets = set('abcdefghijklmnopqrstuvwxyz')
words = set(word)
result = 'YES'
for n in alphabets:
    if n not in words:
        result = 'NO'
print(result)
    