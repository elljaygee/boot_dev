def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        # args is a tuple of positional args e.g. ("# Hello", "## World")
        # run convert_md_to_txt on every item in the tuple
        new_args = list(map(convert_md_to_txt, args))
        
        # kwargs is a dict of named args e.g. {"title": "# My Doc"}
        # .items() breaks it into pairs e.g. [("title", "# My Doc")]
        # lambda keeps the key, cleans the value e.g. ("title", "My Doc")
        # dict() converts the pairs back into a dictionary
        new_kwargs = dict(map(lambda item: (item[0], convert_md_to_txt(item[1])), kwargs.items()))
        
        # call the original function with the cleaned arguments
        return func(*new_args, **new_kwargs)
    
    return wrapper


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)


# BootDev solution:
# def markdown_to_text_decorator(func):
#     def wrapper(*args, **kwargs):
#         converted_args = list(map(convert_md_to_txt, args))

#         def kwarg_item_to_txt(item_tuple):
#             key, value = item_tuple
#             return (key, convert_md_to_txt(value))

#         converted_kwargs = dict(map(kwarg_item_to_txt, kwargs.items()))
#         return func(*converted_args, **converted_kwargs)

#     return wrapper