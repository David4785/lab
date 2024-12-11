from collections import Counter

def can_form_palindrome(string):
    string = string.lower().replace(" ", "")
    char_counts = Counter(string)

    odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)
    return odd_count <= 1

print(can_form_palindrome("civic"))
