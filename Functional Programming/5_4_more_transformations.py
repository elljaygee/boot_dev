def doc_format_checker_and_converter(conversion_function, valid_formats):
    def checker_function(filename, content):
        extension = filename.split(".")[-1]
        if extension in valid_formats:
            result = conversion_function(content)
            return result
        else:
            raise ValueError ("invalid file format")
    return checker_function


# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
