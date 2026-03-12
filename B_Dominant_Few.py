t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    elit = arr[-1]
    crowd = arr[0] + arr[1]
    
    e = 1
    c = 2
    l = n - 2
    r = 2
    possible = elit > crowd
    while not possible and l >= r:
        elit += arr[1]
        crowd += arr[r]
        e += 1
        c += 1
        if e < c and elit > crowd:
            possible = True
        l -= 1
        r += 1
    print('YES' if possible else 'NO') 
            
        
        
        
          
         
        
    
    
            
            