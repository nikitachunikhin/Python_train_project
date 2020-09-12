def complete_series(list):
    """
    You are given an array of non-negative integers,
    your task is to complete the series from 0 to the highest number in the array.
    If the numbers in the sequence provided are not in order you should order them,
    but if a value repeats, then you must return a sequence with only one item,
    and the value of that item must be 0.

    """
    if len(list) > len(set(list)):
        return [0]
    else:
        list_max = max(list)
        list = [i for i in range(0, list_max + 1)]
        return list
