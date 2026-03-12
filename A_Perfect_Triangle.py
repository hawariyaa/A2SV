t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = min(arr[i+2] - arr[i] for i in range(n-2))
    print(ans)