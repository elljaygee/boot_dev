from functools import reduce


def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence

def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    else:
        list = sentences[:n]
        result = reduce(join, list)
        return result + "."
    

# bootdev solution
# import functools


# def join(doc_so_far, sentence):
#     return doc_so_far + ". " + sentence


# def join_first_sentences(sentences, n):
#     if n == 0:
#         return ""
#     return functools.reduce(join, sentences[:n]) + "."
