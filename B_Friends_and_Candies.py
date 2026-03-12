t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    if total % n != 0:
        print(-1)
    else:
        target = total // n
        count = 0
        for candid in arr:
            if candid > target:
                count += 1
        print(count)