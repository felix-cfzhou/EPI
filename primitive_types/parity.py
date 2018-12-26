# Brute Force O(n)
def parity(x):
    result = 0
    while x:
        result ^= x&1
        x >>= 1
    return result

# O(k) k is number of bits
def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x-1
    return result

# O(n\L) n is wordsize L is width of cache
# we can precompute the parity for smaller number of bits and simply lookup the result
