n, t = map(int, input().split())
books = list(map(int, input().split()))

sum1 = 0
left = 0
max_books = 0

for i in range(n):
    sum1 += books[i]
    while sum1 > t:
        sum1 -= books[left]
        left += 1
    max_books = max(max_books, i - left + 1)
print(max_books)