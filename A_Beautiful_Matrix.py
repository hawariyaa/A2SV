
count  = 0
for i in range(5):
    nums = list(map(int, input().split()))
    for j in range(5):
        if nums[j] == 1:
            count = abs(2 - i) + abs(2 - j)
print(count)