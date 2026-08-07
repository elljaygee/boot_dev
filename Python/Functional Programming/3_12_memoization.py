def word_count_memo(document, memos):
    copy_memos = memos.copy()
    if document in copy_memos:
        return copy_memos[document], copy_memos
    doc_count = word_count(document)
    copy_memos[document] = doc_count
    return doc_count, copy_memos
        


# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count


