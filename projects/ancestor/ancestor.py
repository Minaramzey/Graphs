from util import Queue

def earliest_ancestor(ancestors, starting_node):
    queue = Queue()
    current = starting_node
    cache = {}
    for ancestor in ancestors: 
        parent = ancestor[0]
        child = ancestor[1]
        if child not in  cache:
            cache[child] = parent
    if starting_node not in cache:
        return -1
    print(cache)
    has_parent = True
    temp = cache[starting_node]
    while has_parent:
        if cache.get(temp) is not None:
            temp = cache.get(temp)
        else:
            has_parent = False
    return temp