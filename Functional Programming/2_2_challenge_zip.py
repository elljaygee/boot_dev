valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line

# filter is a built-in Python function that creates an iterator containing only 
# elements for which a function returns True.

# lambda pair: pair[1] in valid_formats is an anonymous function (lambda) that:

# Takes a parameter called pair (which will be each tuple from the zipped list)
# Extracts the second element of the tuple with pair[1] (the document format)
# Checks if that format is in the valid_formats list using in valid_formats
# Returns True if the format is valid, False otherwise
# pairs is your iterable (the result of zipping the doc_names and doc_formats lists)

def pair_document_with_format(doc_names, doc_formats):
    pairs = zip(doc_names, doc_formats)
    filtered_pairs = filter(lambda pair: pair[1] in valid_formats, pairs)
    return list(filtered_pairs)

# bootdev solution:
# def pair_document_with_format(doc_names, doc_formats):
#     zipped = list(zip(doc_names, doc_formats))
#     return list(filter(lambda x: x[1] in valid_formats, zipped))
