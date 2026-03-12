n = int(input())
for i in range(n):
    w = input().strip()
    r = len(w)
    if r > 10:
        print(w[0] + str(r - 2) +w[r - 1])
    else:
        print(w)