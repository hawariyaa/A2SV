n,m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


ans = []
for i in range(len(arr2)):
    left = 0
    while left < m and arr2[i] > arr1[left]:
            left += 1
    ans.append(left)
print(*ans)
            
            
        
    
        
    
    