n = int(input())
arr = list(map(int, input().split()))
s = 0
d = 0
l = 0
r = n - 1
turn = 0
while l <= r:
    if arr[l] > arr[r]:
        card = arr[l]
        l += 1
    else:
        card = arr[r]
        r -= 1
    if turn == 0:
        s += card
    else:
        d += card
    turn = 1 - turn
print(s,d)
    