def get_count():
    num_vowels = 0
    for c in input_str:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            num_vowels += 1
    return num_vowels