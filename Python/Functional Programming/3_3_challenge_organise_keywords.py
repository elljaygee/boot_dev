def map_keywords(document, document_map):
    document_map_copy = document_map.copy()
    if document in document_map_copy:
        return document_map_copy[document], document_map_copy
    found_keywords = find_keywords(document)
    document_map_copy[document] = found_keywords
    return found_keywords, document_map_copy


def find_keywords(document):
    keywords = [
    "functional",
    "immutable",
    "declarative",
    "higher-order",
    "lambda",
    "deterministic",
    "side-effects",
    "memoization",
    "referential transparency",
    ]
    found_keywords = []
    document_lowercase = document.lower()
    for keyword in keywords:
        if keyword in document_lowercase:
            found_keywords.append(keyword)
    print(found_keywords)
    return found_keywords

"""
bootdev solution:

def map_keywords(document, document_map):
    new_document_map = document_map.copy()
    if document in new_document_map:
        return new_document_map[document], new_document_map
    found_keywords = find_keywords(document)
    new_document_map[document] = found_keywords
    return found_keywords, new_document_map


def find_keywords(document):
    keywords = [
        "functional",
        "immutable",
        "declarative",
        "higher-order",
        "lambda",
        "deterministic",
        "side-effects",
        "memoization",
        "referential transparency",
    ]
    lowered_doc = document.lower()
    return list(filter(lambda keyword: keyword in lowered_doc, keywords))

"""