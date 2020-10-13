def parse(strng):
    # total = 0
    # if strng == "IX":
    #     return 9
    # elif 'V' not in strng:
    #     return len(strng)
    # elif strng[0] == 'V':
    #     return 5 + (len(strng) - 1)
    # else:
    #     return 5 - (len(strng) - 1)
    return recursive_parse(strng)

def recursive_parse(strng):
    numerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    if strng == "":
        return 0
    for key in numerals:
        pre_value = 0
        key_value = 0
        post_value = 0

        if key not in strng:
            pass
        elif key == "I":
            return len(strng)
        else:
            pre_string = strng[:strng.index(key)]
            if len(pre_string) > 0:
                pre_value = recursive_parse(pre_string)
            current_index = strng.index(key)
            while strng[current_index] == key:
                current_index += 1
                if current_index > len(strng) - 1:
                    break
            last_index = current_index - 1
            key_value = (last_index - strng.index(key) + 1) * numerals[key]
            if last_index < len(strng) - 1:
                post_string = strng[(last_index + 1):]
                post_value = recursive_parse(post_string)
            return key_value + post_value - pre_value
