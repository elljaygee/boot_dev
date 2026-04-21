default_commands = {}
default_formats = ["txt", "md", "html"]
saved_documents = {}

# Don't edit above this line

def add_custom_command(commands, new_command, function):
    commands_copy = commands.copy()
    commands_copy[new_command] = function
    return commands_copy


def add_format(formats, format):
    formats_copy = formats.copy()
    formats_copy.append(format)
    return formats_copy


def save_document(docs, file_name, doc):
    docs_copy = docs.copy()
    docs_copy[file_name] = doc
    return docs_copy


def add_line_break(line):
    return(line + "\n\n")

# bootdev solution is identical!