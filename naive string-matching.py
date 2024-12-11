T = "acaabc"
n = len(T)
P = "aab"
m = len(P)
temp = []
for s in range(n-m+1):
        if T[s:s+m] == P:
            temp.append(s)
print("s = ", s)