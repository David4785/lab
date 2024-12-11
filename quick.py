def partition(list, left, right):
    pivot = list[right]
    i = left - 1

    for j in range(left, right):
        if list[j] <= pivot:
            i = i + 1
            list[i], list[j] = list[j], list[i]

    list[i + 1], list[right] = list[right], list[i + 1]
    return i + 1

def quick_sort(list, left, right):
    if left < right:
        pi = partition(list, left, right)
        quick_sort(list, left, pi - 1)
        quick_sort(list, pi + 1, right)

list = [10, 7, 8, 9, 1, 5]
n = len(list)
quick_sort(list, 0, n - 1)
print("Sorted list = ", list)