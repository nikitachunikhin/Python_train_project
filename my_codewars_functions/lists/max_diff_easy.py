def max_diff(lst):
    """
    You must implement a function maxDiff that return the difference between the biggest
    and the smallest value in a list(lst) received as parameter.
    The list(lst) contains integers,
    that means it may contain some negative numbers.
    If the list is empty or contains a single element,
    return 0.
    The list(lst) is not sorted.

    :param lst: list of integers
    :return:
    """
    if len(lst) > 0:
        lst.sort()
        res = lst[-1] - lst[0]
        return res
    else:
        return 0
