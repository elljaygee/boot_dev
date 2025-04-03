def file_type_getter(file_extension_tuples):
    ext_dict = {}
    for entry in file_extension_tuples:
        file_type = entry[0]
        extensions = entry[1]
        for ext in extensions:
            ext_dict[ext] = file_type
    # lambda function takes the extension given in the test and returns the file type from the dict
    return lambda extension: ext_dict.get(extension, "Unknown")

# BootDev solution:

# def file_type_getter(file_extension_tuples):
#     file_extensions_dict = {}
#     for tup in file_extension_tuples:
#         for ext in tup[1]:
#             file_extensions_dict[ext] = tup[0]
#     return lambda ext: file_extensions_dict.get(ext, "Unknown")
