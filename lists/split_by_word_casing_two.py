def replace_symbols(input_string, symbols_list, new_string):
    for elem in symbols_list:
        if elem in input_string:
            input_string = input_string.replace(elem, new_string)
    return input_string


def lower_case(current_word):
    lower = True
    for letter in current_word:
        if ord(letter) < 97 or ord(letter) > 122:
            lower = False
    return lower


def upper_case(curr_word):
    upper = True
    for letter in curr_word:
        if ord(letter) < 65 or ord(letter) > 90:
            upper = False
    return upper


if __name__ == "__main__":
    text = input()
    symbols = [',', ';', ':', '.', '!', '(', ')', '"', "'", '\\', "/", "[", "]"]
    result = replace_symbols(text, symbols, " ")

    lst = result.split()

    lower_case_list = []
    upper_case_list = []
    mixed_case_list = []

    for word in lst:
        if lower_case(word):
            lower_case_list.append(word)
        elif upper_case(word):
            upper_case_list.append(word)
        else:
            mixed_case_list.append(word)

    print(f"Lower-case: ", end="")
    print(", ".join(lower_case_list))
    print(f"Mixed-case: ", end="")
    print(", ".join(mixed_case_list))
    print(f"Upper-case: ", end="")
    print(", ".join(upper_case_list))
