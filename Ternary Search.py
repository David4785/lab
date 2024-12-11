def ternary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            high = mid1 - 1
        elif target > arr[mid2]:
            low = mid2 + 1
        else:
            low, high = mid1 + 1, mid2 - 1

    return -1
arr = [6, 100, 500, 1000, 15000]
target = 1000

result = ternary_search(arr, target)
if result != -1:
    print(f"Գտնվեց {result}֊րդ ինդեքսում")
else:
    print("Չգտնվեց")
