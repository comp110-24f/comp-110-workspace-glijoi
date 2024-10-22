def add_at_index(vals: list[int], elem: int, index: int) -> None:
    """modifies input list to put elem at index"""
    if (index < 0) or (index > len(vals)):
        raise IndexError("Index is out of bounds for the input list")
    elif (index == 0) and (len(vals) == 0):
        vals.append(elem)
    elif index == len(vals) + 1:
        vals.append(elem)
    else:
        vals[index] = elem
