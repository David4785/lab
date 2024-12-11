def binary_search(arr, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
#2b
    n = len(arr)
    bound = 1
    while bound < n and arr[bound] < target:
        bound *= 2
    return binary_search(arr, bound // 2, min(bound, n - 1), target)

arr = [6, 100, 500, 1000, 15000]
target = 15000

result = exponential_search(arr, target)

if result != -1:
    print(f"Գտնվեց {result}֊րդ ինդեքսում")
else:
    print("Չգտնվեց")