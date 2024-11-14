def is_ancestor(l, a, b):
    parents = []
    for arc in l:
        if arc[1] == a:
            parents.append(arc[0])

    if not parents:
        return False
    elif b in parents:
        return True
    else:
        for parent in parents:
            if is_ancestor(l, parent, b):
                return True
        return False

def is_ancestor_benjamin(l, search_number, ancestor):
    result = None
    for n in l:
        if n[0] == ancestor and n[1] == search_number:
            return True
        if n[0] == search_number:
            result = n[1]
        elif n[1] == search_number:
            result = n[0]
        if result and n[1] == result and n[0] == ancestor:
            return True
    return False

def find_ancestors(l,elem):
    return [arc[0] for arc in l if arc[1]==elem]

def is_ancestor_oops(l,a,b):
    ancestors=find_ancestors(l,a)
    while ancestors:
        if b in ancestors:
            return True
        elem=ancestors.pop()
        ancestors += find_ancestors(l,elem)
    return  False

L = [(1, 4), (4, 5), (7, 8), (0, 2), (3, 1), (2, 6), (0, 1)]

print(is_ancestor_oops(L, 5, 3))
print(is_ancestor_oops(L, 4, 6))