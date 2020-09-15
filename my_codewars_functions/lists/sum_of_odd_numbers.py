def row_sum_odd_numbers(n):
    """Given the triangle of consecutive odd numbers:
                   1
                3     5
             7     9    11
         13    15    17    19
      21    23    25    27    29

        Calculate the row sums of this triangle from the row index (starting at index 1) e.g.
    """
    first_num = ((n * (n - 1)) + 1)
    last_num = first_num + (n - 1) * 2
    lst = [i for i in range(first_num, last_num + 1, 2)]
    theSum = 0
    for i in lst:
        theSum = theSum + i
    return theSum