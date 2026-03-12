n,m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
first, second = 0,0
ans = []
while first < len(arr1) and second < len(arr2):
    if arr1[first] < arr2[second]:
        ans.append(arr1[first])
        first += 1
    else:
        ans.append(arr2[second])
        second += 1
ans.extend(arr2[second:])
ans.extend(arr1[first:])

print(*ans)
    
    