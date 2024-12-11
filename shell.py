def func(list):
    n = len(list)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = list[i]
            j = i
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        gap //= 2

list = [12, 34, 5, 2, 3]
func(list)
print("Sorted list = ", list)