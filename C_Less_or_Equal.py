n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
if k==0:
    if arr[0] - 1 >= 1:
        print(arr[0] - 1)
    else:
        print(-1)
else:
    ans = arr[k-1]
    if k < n and arr[k] == ans:
        print(-1)
    else:
        print(ans)

    