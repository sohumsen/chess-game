# enabled globally due to their usefulness

def algebra_to_cartesian(coordstr):
    """ coord is a string like a1 """
    x = ord(coordstr[0]) - 97
    y = 8 - int(coordstr[1])
    return x, y

def cartesian_to_algebra(tup):
    """ tup is a tuple """
    x = tup[0]  # 0
    y = tup[1]  # 7
    new_coord = chr(x + 97) + str(8 - y)
    return new_coord
