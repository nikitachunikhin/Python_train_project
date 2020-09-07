def get_positions(text):
    for char in text:
        pos = ord(char)
        if pos >= 65 and pos <= 90:
            yield pos - 64
        if pos >= 97 and pos <= 122:
            yield pos - 96

def alphabet_position(text):
    # return " ".join((str(char) for char in get_positions(text)))
    res_list = [str(char) for char in get_positions(text)]
    # print(res_list)
    res = " ".join(res_list)
    return res

if __name__ == '__main__':
    out = alphabet_position(text='Adianfaifk')
    print(out)