def codes(tree, prefix=""):
    if len(tree) == 1:
        yield (tree, prefix)
        return
    for bit, child in zip("01", tree):
        for pair in codes(child, prefix + bit):
            yield pair