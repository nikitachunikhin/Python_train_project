def remove_every_other(my_list):
    """
    Take an array and remove every second element from the array. Always keep the first element and start removing
    with the next element.

    :param my_list: list
    :return: list
    """
    if type(my_list) == list:
        return my_list[::2]
    else:
        return []


if __name__ == '__main__':
    my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep']
    res = remove_every_other(my_list)
    print(res)