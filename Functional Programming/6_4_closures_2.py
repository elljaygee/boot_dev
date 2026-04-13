def new_collection(initial_docs):
    copy_docs = initial_docs.copy()

    def add_doc(string):
        copy_docs.append(string)
        return copy_docs

    return add_doc
