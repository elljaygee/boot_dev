def get_median_font_size(font_sizes):
    ordered_list = sorted(font_sizes)
    list_len = len(ordered_list)
    index = (list_len - 1) // 2
    if list_len == 0:
        return None
    else:
        return (ordered_list[index])

# boot.dev solution:

def get_median_font_size(font_sizes):
    if len(font_sizes) == 0:
        return None
    return sorted(font_sizes)[(len(font_sizes) - 1) // 2]
