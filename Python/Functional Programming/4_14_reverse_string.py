def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])
        

"""
bootdev solution:

def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]
"""