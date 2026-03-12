n, s = map(int, input().split())
num1 = list(map(int, input().split()))
left = 0
max_len = 0
sum1 = 0
for i in range(len(num1)):
    sum1 += num1[i]
    while sum1 > s:
        sum1 -= num1[left]
        left += 1
    max_len = max(max_len, i-left+1)
print(max_len)
        
    
    