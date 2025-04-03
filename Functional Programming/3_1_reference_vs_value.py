import copy 

def add_format(default_formats, new_format):
    copy_default_formats = copy.copy(default_formats)
    copy_default_formats[new_format] = True
    return copy_default_formats


def remove_format(default_formats, old_format):
    copy_default_formats = copy.copy(default_formats)
    copy_default_formats[old_format] = False
    return copy_default_formats

# bootdev solution:

# def add_format(default_formats, new_format):
#     new_formats = default_formats.copy()
#     new_formats[new_format] = True
#     return new_formats


# def remove_format(default_formats, old_format):
#     new_formats = default_formats.copy()
#     new_formats[old_format] = False
#     return new_formats