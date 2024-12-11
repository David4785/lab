def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

arr = [100, 500, 1000, 15000, 6]
target = 1000

result = linear_search(arr, target)
if result != -1:
    print(f"Գտնվեց {result}֊րդ ինդեքսում")
else:
    print("Չգտնվեց")
