# right propagate right most set bit
def right_prop(x):
    return x | x-1


# compute x mod a power of 2
def mod2(x, mod):
    return x & ((mod | mod-1) >> 1)


# check if x is a power of 2
def is_pow2(x):
    return not x & x-1
