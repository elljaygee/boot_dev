def restore_documents(originals, backups):
    return set(filter(lambda x: not x.isdigit(), map(lambda x: x.upper(), originals + backups)))

# multi-line function:
# def restore_documents(originals, backups):
#     # Step 1: Combine the two tuples of documents
#     combined_docs = originals + backups
    
#     # Step 2: Convert all documents to uppercase for case-insensitive comparison
#     uppercase_docs = map(lambda x: x.upper(), combined_docs)
    
#     # Step 3: Filter out corrupted documents (those containing only digits)
#     valid_docs = filter(lambda x: not x.isdigit(), uppercase_docs)
    
#     # Step 4: Convert to a set to remove duplicates
#     unique_docs = set(valid_docs)
    
#     return unique_docs

# bootdev solution:

# def restore_documents(originals, backups):
#     return set(
#         filter(
#             lambda doc: not doc.isdigit(),
#             map(lambda doc: doc.upper(), originals + backups),
#         )
#     )
