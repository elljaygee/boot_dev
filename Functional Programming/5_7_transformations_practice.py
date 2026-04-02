def get_filter_cmd(filter_one, filter_two):
    
    def filter_cmd(content, option="--one"):

        if option == "--one":
            return filter_one(content)
        elif option == "--two":
            return filter_two(content)
        elif option =="--three":
            first = filter_one(content)
            return filter_two(first)
        else:
            raise Exception ("invalid option")
            

    return filter_cmd


# don't touch below this line


def replace_bad(text):
    return text.replace("bad", "good")


def replace_ellipsis(text):
    return text.replace("..", "...")


def fix_ellipsis(text):
    return text.replace("....", "...")
