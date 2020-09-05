def remove_every_other(my_list):
    if type(my_list) == list:
        return my_list[::2]
    else:
        return []


if __name__ == '__main__':
    my_list = ['fdfd']
    res = remove_every_other(my_list)
    print(res)