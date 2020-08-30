def strrr(a):
    c = a.capitalize()
    return c


def first_letter_upper(a):
    first_letter = a[0]
    first_letter = first_letter.upper()
    letters = a[1:]
    letters = letters.lower()
    new_string = first_letter + letters
    return new_string


def poz_index(i, example):
    if (i < 0) and (i >= -1 * len(example)):
        poz_i = len(example) + i
    elif (i >= 0) and (i < len(example)):
        poz_i = i
    else:
        poz_i = False
    return poz_i


if __name__ == '__main__':
    example = 'knfdjSFj8 78S'
    # new = first_letter_upper(example)
    # print(new)

    k = 2
    i = 255

    # version 1
    # pos_k = poz_index(k, example)
    # pos_i = poz_index(i, example)
    #
    # if pos_k and pos_i and (pos_k < pos_i):
    #     result = example.endswith(example[i - 1], k, i)
    #     print(result)
    # else:
    #     print('result = False or i - out of string')

    # version 2
    if example[k:i] and (i < len(example)):
        result = example.endswith(example[i - 1], k, i)
        print(result)
    else:
        print('result = False or i - out of string')
