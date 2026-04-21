def zipmap(keys, values):
    zipped ={}
    print(f'keys {keys} values {values}')
    if(len(keys) == 0 or len(values) == 0):
        notzipped = {}
        return notzipped
    else:
        if(len(keys) != 1):
            zipped[keys[0]] = values[0]
            zipped = zipmap(keys[1:], values[1:])
        zipped[keys[0]] = values[0]
        return zipped
    
"""
bootdev solution:

def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}
    res = zipmap(keys[1:], values[1:])
    res[keys[0]] = values[0]
    return res
"""