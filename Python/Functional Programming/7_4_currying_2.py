def lines_with_sequence(char):
    
    def with_char(length):
        sequence = char * length

        def with_length(doc):
            counter = 0
            lines = doc.splitlines()
            for line in lines:
                if sequence in line:
                    counter += 1
            return counter

        return with_length

    return with_char
