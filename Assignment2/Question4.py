def countarr(arr, target_sum):
    count = 0
    left = 0
    right = len(arr) - 1
    arr.sort()

    while left < right :
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            count += 1
            left += 1
            right -= 1

        elif current_sum < target_sum:
            left += 1

        else:
            right -= 1

    return count

pri=countarr([1,5,7,5,1,-1],6)
print(pri)