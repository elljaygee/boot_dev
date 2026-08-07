def find_longest_word(document, longest_word=""):
    if (len(document.strip())) == 0:
        return longest_word

    words = document.split()
    
    if len(words[0]) > len(longest_word):
        longest_word = words[0]

    return find_longest_word(' '.join(words[1:]), longest_word)

"""
If the document (after stripping whitespace) is empty, the function returns whatever is currently stored in longest_word. This is our base case for the recursion.
The document is split into a list of words using document.split().
The first word (words[0]) is compared to the current longest_word. If it's longer, it becomes the new longest_word.
Then comes the recursive magic: the function calls itself with two arguments:
The rest of the document (all words except the first one), joined back into a string
The current longest_word (which might have been updated)
This process repeats until there are no more words in the document.
Flaw: will error if the list is empty as words[0] will not return anything.

bootdev solution:

def find_longest_word(document, longest_word=""):
    if len(document) == 0:  # handles empty list
        return longest_word
    words = document.split(maxsplit=1)
    if len(words) < 1:
        return longest_word
    first_word = words[0]
    if len(first_word) > len(longest_word):
        longest_word = first_word
    if len(words) < 2:
        return longest_word
    return find_longest_word(words[1], longest_word)

"""