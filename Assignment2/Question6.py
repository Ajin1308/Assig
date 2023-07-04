# Find the Kth largest and Kth smallest number in an array
def large_and_small(arr , k):
    arr.sort()
    print(arr)
    arr_smallest = arr[k-1]
    arr_largest = arr[-k]
    return arr_largest,arr_smallest

large, small=large_and_small([9,5,6,3,2,7], 3)
print(small)
print(large)