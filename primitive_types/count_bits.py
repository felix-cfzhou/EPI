# Brute Force O(n)
def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x&1
        x >>= 1
    return num_bits

# O(k) k is number of bits
def count_bits(x):
    num_bits = 0
    while x:
        num_bits += 1
        x &= x-1
    return num_bits
