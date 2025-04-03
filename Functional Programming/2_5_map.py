def change_bullet_style(document):
    lines_list = document.split("\n")
    bullets_changed = map(convert_line, lines_list)
    rejoined_doc = "\n".join(bullets_changed)
    return rejoined_doc
    


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line

# bootdev solution:
# def change_bullet_style(document):
#     return "\n".join(map(convert_line, document.split("\n")))
