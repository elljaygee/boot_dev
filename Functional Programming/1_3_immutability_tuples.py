def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    documents = documents + (new_doc,) # creating a copy of a tuple with the new item added
    return documents
