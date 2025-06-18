def sum_nested_list(lst):
    n = 0
    for item in lst:
        if isinstance(item, list) == False:
            n += item
        if isinstance(item, list) == True:
            total_size = sum_nested_list(item)
            n+= total_size
    return n

"""bootdev solution:
def sum_nested_list(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):
            total += sum_nested_list(element)
        else:
            total += element
    return total
"""