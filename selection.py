list = [64, 34, 25, 12, 22, 11, 90]
n = len(list)

for i in range(n):
    min = i
    for j in range(i+1, n):
        if list[j] < list[min]:
            min = j
    if min != i:
        list[i],list[min] = list[min],list[i]
print(list)