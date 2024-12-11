import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1

arr = [6, 100, 500, 1000, 15000]
target = 1000
result = jump_search(arr, target)
if result != -1:
    print(f"Գտնվեց {result}֊րդ ինդեքսում")
else:
    print("Չգտնվեց")