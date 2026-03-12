n,m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


ans = []
left = 0
for i in range(len(arr2)):  
    while left < n and arr2[i] > arr1[left]:
            left += 1
    ans.append(left)
print(*ans)
            
            
        
    
        
    
    