n = int(input())
arr = list(map(int, input().split()))
sum_serj = 0
sum_dima = 0
left = 0
right = len(arr) - 1
count = 0
while left <= right:
    if arr[left] > arr[right]:
        if count % 2 == 0:
           sum_serj += arr[left]
        else:
            sum_dima += arr[left]
        left += 1
    else:
        if count % 2 == 0:
           sum_serj += arr[right]
        else:
            sum_dima += arr[right]
        right -= 1
    count += 1
print(sum_serj, sum_dima)
