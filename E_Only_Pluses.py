t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    max_product = 0
    
    for da in range(6):  # 0 to 5
        for db in range(6 - da):
            dc = 5 - da - db
            na = a + da
            nb = b + db
            nc = c + dc
            product = na * nb * nc
            if product > max_product:
                max_product = product
    
    print(max_product)