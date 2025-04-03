def deduplicate_lists(lst1, lst2, reverse=False):
    new_list = []
    for x in lst1 + lst2:
        if x not in new_list:
            new_list.append(x)

    return sorted(new_list, reverse=reverse)
