def remove_emphasis_from_word(word):
    word = word.strip("*")
    return word

def remove_emphasis_from_line(line):
    words = line.split()  # This splits by any whitespace
    clean_words = map(remove_emphasis_from_word, words)
    return " ".join(clean_words)  # Join the words back with spaces

def remove_emphasis(doc_content):
    lines = doc_content.split("\n")  # Split by newlines
    clean_lines = map(remove_emphasis_from_line, lines)
    return "\n".join(clean_lines)  # Join back with newlines