def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

arr = [6, 100, 500, 1000, 15000]
target = 15000

result = interpolation_search(arr, target)

if result != -1:
    print(f"Գտնվեց {result}֊րդ ինդեքսում")
else:
    print("Չգտնվեց")