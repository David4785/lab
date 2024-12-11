def pattern_search(substring, main_string):
    def compute_prefix_array(substring):
        prefix_array = [0] * len(substring)
        prefix_length = 0
        index = 1
        while index < len(substring):
            if substring[index] == substring[prefix_length]:
                prefix_length += 1
                prefix_array[index] = prefix_length
                index += 1
            else:
                if prefix_length != 0:
                    prefix_length = prefix_array[prefix_length - 1]
                else:
                    prefix_array[index] = 0
                    index += 1
        return prefix_array

    prefix_array = compute_prefix_array(substring)
    main_index = sub_index = 0
    while main_index < len(main_string):
        if substring[sub_index] == main_string[main_index]:
            main_index += 1
            sub_index += 1
        if sub_index == len(substring):
            print(f"Pattern-ը գտնվել է {main_index - sub_index}֊րդ ինդեքսում")
            sub_index = prefix_array[sub_index - 1]
        elif main_index < len(main_string) and substring[sub_index] != main_string[main_index]:
            if sub_index != 0:
                sub_index = prefix_array[sub_index - 1]
            else:
                main_index += 1

main_string = "abacaabaccabacabaabb"
substring = "abacab"
pattern_search(substring, main_string)
