import re

def fake_bin(x):
    output_res = ''
    x = re.sub("[^0-9]", "", x)
    for i in x:
        if int(i) >= 5:
            output_res = output_res + '1'
        else:
            output_res = output_res + '0'
    return output_res


def fake_bin1(x):
    if x == "":
        return x

    if int(x[0]) < 5:
        return '0' + fake_bin1(x[1:])

    return '1' + fake_bin1(x[1:])

def fake_bin2(x):
    x = re.sub("[^0-9]", "", x)
    x = re.sub("[0-4]", "0", x)
    x = re.sub("[5-9]", "1", x)
    return x

if __name__ == '__main__':
    res = fake_bin2(x='12124657756289745')
    print(res)