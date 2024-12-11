def dict(pattern):
    D = {}
    length = len(pattern)

    for i in range(length):
        D[pattern[i]] = i
    return D

def func(text, pattern):
    m = len(pattern)
    n = len(text)

    D = dict(pattern)

    shift = 0

    while shift <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
        if j < 0:
            print(f"Pattern-ը գտնվում է {shift}֊րդ ինդեքսում")
            shift += (m - D.get(text[shift + m], -1)) if shift + m < n else 1
        else:
            shift += max(1, j - D.get(text[shift + j], -1))

text = "ABAAABCD"
pattern = "ABC"
func(text, pattern)
