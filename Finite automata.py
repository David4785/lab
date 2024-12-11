def build_transition_table(pattern):
    m = len(pattern)
    transition = [{} for _ in range(m + 1)]

    for state in range(m + 1):
        for char in set(pattern):
            if state < m and char == pattern[state]:
                transition[state][char] = state + 1
            else:
                for k in range(state, 0, -1):
                    if pattern[:k] == (pattern[state - k + 1:state] + char):
                        transition[state][char] = k
                        break
                else:
                    transition[state][char] = 0
    return transition

def finite_automaton_search(text, pattern):
    transition = build_transition_table(pattern)
    state = 0
    matches = []

    for i, char in enumerate(text):
        state = transition[state].get(char, 0)
        if state == len(pattern):
            matches.append(i - len(pattern) + 1)

    return matches

text = "aabccbabbca"
pattern = "abbc"

matches = finite_automaton_search(text, pattern)
print(f"Pattern֊ը գտնվում է {matches}֊րդ ինդեքսում")
