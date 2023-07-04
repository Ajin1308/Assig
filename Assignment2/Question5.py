def duplicate(arr):
    arr.sort()
    duplicates = []

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            duplicates.append(arr[i])
    return duplicates

dup = duplicate([1,2,2,3,4,5,5,5,6])
print(dup)