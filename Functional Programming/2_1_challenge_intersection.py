def get_common_formats(formats1, formats2):
    both_formats = set(formats1).intersection(set(formats2))
    return both_formats


# bootdev solution:
# def get_common_formats(formats1, formats2):
#     return set(formats1).intersection(set(formats2))
