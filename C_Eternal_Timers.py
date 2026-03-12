t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    possible = True
    for j in range(n):
        if arr[j] <= 2 * max(j, n - 1 - j):
           possible = False
    print('YES' if possible else 'NO')  
    