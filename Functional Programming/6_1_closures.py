def word_count_aggregator():
    count = 0

    def increment_count(doc):
        nonlocal count
        count += len(doc.split())
        return count

    return increment_count
    
