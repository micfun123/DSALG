baddata = [64, 25, 12, 22, 11, 90, 0, 55]


def SelectionSort(arr):
    for iteration in range(len(arr)):
        min_index = iteration
        for j in range(iteration + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[iteration], arr[min_index] = arr[min_index], arr[iteration]
    return arr


print(SelectionSort(baddata))

def InsertionSort(arr):
    for index in range(1, len(arr)):
        key = arr[index]
        privious_index = index - 1
        while privious_index >= 0 and arr[privious_index] > key:
            arr[privious_index + 1], arr[privious_index] = arr[privious_index], arr[privious_index + 1]
            privious_index = privious_index - 1

    return arr

print(InsertionSort(baddata))

def bubbleSort(arr):
    for index in range(len(arr)):
        for compare_index in range(0, len(arr) - index - 1):
            if arr[compare_index] > arr[compare_index + 1]:
                arr[compare_index], arr[compare_index + 1] = arr[compare_index + 1], arr[compare_index]
    return arr

print(bubbleSort(baddata))

def linearSearch(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

print(linearSearch(baddata,55))
print(linearSearch(baddata,7))

def BinarySearch(arr,target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1

        elif arr[mid] > target:
            high = mid - 1
    return -1

print(BinarySearch(SelectionSort(baddata),12))

def recurseBinarySearch(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recurseBinarySearch(arr, target, mid + 1, high)
    else:
        return recurseBinarySearch(arr, target, low, mid - 1)

print(recurseBinarySearch(SelectionSort(baddata),12))

def TernarySearch(arr,target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        if arr[mid1] > target:
            high = mid1 - 1
        elif arr[mid2] < target:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return -1
print(TernarySearch(SelectionSort(baddata),12))
print(TernarySearch(SelectionSort(baddata),7))

def BinaryToNearst(arr,target):
    low = 0
    high = len(arr) - 1
    if target < arr[low]:
        return arr[low]
    if target > arr[high]:
        return arr[high]
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return arr[mid]
        
        elif arr[mid] < target:
            low = mid + 1

        elif arr[mid] > target:
            high = mid - 1
    if abs(arr[low] - target) < abs(arr[high] - target):
        return arr[low]
    else:
        return arr[high]