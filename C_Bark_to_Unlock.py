word = input().strip()
n = int(input())
arr = []
found = False
for i in range(n):
    arr.append(input().strip())
for w in arr:
    if w == word:
        found = True
        break
start = False
End = False
if not found:
    for n in arr:
        if len(w) == 2:
            if n[1] == word[0]:
               End = True
            if n[0] == word[1]:
               start = True
    if start and End:
        found = True
          
print('YES' if found else 'NO')