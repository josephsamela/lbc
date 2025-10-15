
def flatten(d, parent='', level=0):
    '''
    Flatten nested dictionary of arbitrary depth
    '''
    items = {}

    for k, v in d.items():
        
        if isinstance(v, str):
            continue

        if isinstance(v, dict):
            level+=1
            items.update(flatten(v, k, level))
        else:
            v.key = k
            v.chapter = parent
            items[k] = v

    return items
