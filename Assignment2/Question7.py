def move_negative_elements(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] >= 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] >= 0 and arr[right] >= 0:
            right -= 1
        else:
            left += 1
            right -= 1

    return arr
array = move_negative_elements([-1,-2,3456,-6,6,6])
print(array)

# -----------------------------------------------
# or

# def move_negative_elements(arr):
#     arr.sort()
# array = move_negative_elements([-1,-2,3456,-6,6,6])
# print(array)