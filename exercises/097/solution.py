def love_meet(x, y):
    return set(x) & set(y)


def affair_meet(x, y, z):
    i = set(y) & set(z)
    return i - set(x)
