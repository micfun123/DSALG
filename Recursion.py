
def linFib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def recFib(n):
    if n <= 1:
        return n
    return recFib(n - 1) + recFib(n - 2)

print(linFib(10))  # Output: 55 BigO O(n)
print(recFib(10))  # Output: 55 BigO O(2^n)



def recGCD(a, b):
    if b == 0:
        return a
    return recGCD(b, a % b)


print(recGCD(48, 18))  # Output: 6



def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = mergesort(arr[:mid])
    right_half = mergesort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1

        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

print(mergesort([38, 27, 43, 3, 9, 82, 10]))  # Output: [3, 9, 10, 27, 38, 43, 82]



def recpalindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return recpalindrome(s[1:-1])
print(recpalindrome("racecar"))  # Output: True
print(recpalindrome("hello"))    # Output: False


