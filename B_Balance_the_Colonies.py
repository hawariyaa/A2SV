n = int(input())
for _ in range(n):
    t = int(input())
    if t <= 3:
        print(t)
    elif t % 2 == 0:
        print(0)
    else:
        print(1)
        
       