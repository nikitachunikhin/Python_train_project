def even_chars(st):
    if st:
        if (len(st)>=2) and (len(st)<100):
            a = st[1:(len(st) + 1):2]
            a = list(a)
            return a
        else:
            return 'invalid string'
    else:
        return 'invalid string'

def even_chars1(st):
    if (st) and (len(st)>=2) and (len(st)<=100):
        a = st[1:(len(st) + 1):2]
        a = list(a)
        return a
    else:
        return 'invalid string'

def even_chars2(st):
    return [ x for i, x in enumerate(st) if i%2 == 1] if 101 > len(st) > 1 else "invalid string"

if __name__ == '__main__':
    # res = even_chars1(st=None)
    # print(res)
    for i, x in enumerate('fdfdgsg dvsijubguh'):
        print(i, x)