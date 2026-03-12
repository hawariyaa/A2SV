n = int(input())
for _ in range(n):
    n, m, p, q = map(int, input().split())
    k = n // p
    r = n % p
    if r == 0:
        print("YES" if m == k * q else "NO")
    else:
        print("YES")