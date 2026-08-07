import copy

def css_styles(initial_styles):
    styles_copy = copy.deepcopy(initial_styles)

    def add_style(selector, property, value):
        if selector in styles_copy:
            styles_copy[selector][property] = value
        else:
            styles_copy[selector] = {property : value}
        return styles_copy

    return add_style

# BootDev solution:

# import copy


# def css_styles(initial_styles):
#     styles = copy.deepcopy(initial_styles)

#     def add_style(selector, property, value):
#         if selector not in styles:
#             styles[selector] = {}
#         styles[selector][property] = value
#         return styles

#     return add_style
