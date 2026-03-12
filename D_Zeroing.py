n,t = map(int, input().split())
for _ in range(t):
    arr = list(map(int, input().split()))
    arr.sort()
    i = 0
    while i < t:
        sub = 0
        op = arr[i] 
        for j in range(len(arr)):
            arr[j] = arr[j] - op
        print(arr[j])
        
            