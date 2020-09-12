def remove_duplicates_from_list(input_list):
    list_no_duplicates = []
    for elem in input_list:
        if elem not in list_no_duplicates:
            list_no_duplicates.append(elem)
    return list_no_duplicates

def days_represented(trips):
    """
    How many days are we represented in a foreign country?

    My colleagues make business trips to a foreign country. We must find the number of days our company is
    represented in a country. Every day that one or more colleagues are present in the country is a day that the
    company is represented. A single day cannot count for more than one day. Write a function that recieves a list of
    pairs and returns the number of days that the company is represented in the foreign country. The first number of
    the pair is the number of the day of arrival and the second number of the pair is the day of departure of someone
    who travels, i.e. 1 january is number 1 and 31 of december is 365.

    :param trips: list of lists wit 2 elements, for example: [[10,15],[25,35],[25,35]]
    :return: integer

    """
    trips = remove_duplicates_from_list(trips)  # remove duplicates from list

    days = []
    for trip in trips:
        if trip[0] < trip[1]:  # exclude trip it end earlier than begin
            new_list = [i for i in range(trip[0], trip[1]+1)]
            days = days + new_list

    days = list(set(days))  # unique days only
    result = len(days)
    return result

def days_represented_ver2(trips):
    l = [0]*366
    for trip in trips:
        for i in range(trip[0], trip[1]+1):
            l[i] = 1
    return sum(l)

def days_represented3(trips):
    days = set()
    for trip in trips:
        if trip[0] < trip[1]:  # exclude trip it end earlier than begin
            for i in range(trip[0], trip[1]+1):
                days.add(i)


    result = len(days)
    return result

if __name__ == '__main__':
    trips = [[182, 201], [139, 162], [127, 162], [152, 169], [298, 299], [75, 78], [266, 285], [288, 316], [255, 278], [225, 257], [82, 101]]
    res = days_represented(trips)
    print(res)

    res2 = days_represented_ver2(trips)
    print(res2)

    res3 = days_represented3(trips)
    print(res3)




