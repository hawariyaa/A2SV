n, t = map(int, input().split())
books = list(map(int, input().split()))
books.sort()
sum = 0
count = 0

for i in range(n):
    sum += books[i]
    if sum <= t:    
        count += 1
    else:
        break
print(count)