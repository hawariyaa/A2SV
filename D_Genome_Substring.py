n = int(input())
s = input().strip()
T = "ACTG"
min_distance = float('inf')
for i in range(n-3):
    count = 0
    for j in range(4):
        d = abs(ord(s[i + j]) - ord(T[j]))
        count += min(d, 26 - d)
    min_distance = min(min_distance, count)
print(min_distance)
        
        
    
    