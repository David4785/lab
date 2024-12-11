list = [64, 34, 25, 12, 22, 11, 90]

n = len(list)
for i in range(n):
    for j in range(0, n - i - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]

print("sorted list = ", list)