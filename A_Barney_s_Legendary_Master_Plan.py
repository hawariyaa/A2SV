t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    d_positive = set()
    for i in arr:
        if i > 0:
            d_positive.add(i)
    k = len(d_positive)
    if k == 0:
        print(0)
    else:
        print(2 * k - 1)
    