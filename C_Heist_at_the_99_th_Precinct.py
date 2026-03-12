t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    mx = max(arr)
    count = arr.count(mx)
    if count % 2 == 1:
        print('YES')
    else:
        print('NO')