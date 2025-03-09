def format_line(line):
    # original:
    # return f"{line.rstrip().capitalize().replace(',', '')}...."

    # corrected:
    return f"{line.strip().upper().replace('.', '')}..."
    
    # testing each step
    # strip_line = line.strip()
    # print(strip_line)
    # add_capitals = strip_line.upper()
    # print(add_capitals)
    # remove_periods = add_capitals.replace('.', '')
    # print(remove_periods)
    # add_ellipses = remove_periods + '...'
    # print(add_ellipses)

    # return add_ellipses
    
    