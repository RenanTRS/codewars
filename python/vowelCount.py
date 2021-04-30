def get_count():
    num_vowels = 0
    for c in input_str:
        if c in 'aeiou':
            num_vowels += 1
    return num_vowels