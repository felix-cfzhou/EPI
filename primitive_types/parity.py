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


# O(log n) n is word wize, we use associativity of XOR
def parity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1
