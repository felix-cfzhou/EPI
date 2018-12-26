# swap right most consecutive bits that differ O(n) n is wordsize
def closest_int_same_bit_count(x):
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS - 1):
        if ((x >> i) & 1) != ((x >> (i+1)) & 1):
            x ^= (1 << i) | (1 << (i+1))
            return x

    raise ValueError('All bits are 0 or 1')


# O(1) solution
def closest_int_same_bit_count(x):
    lowest_set_bit = x & ~(x-1)
    if lowest_set_bit & 1:
        lowest_unset_bit = (~x) & ~(~x-1)
        return x ^ (lowest_unset_bit | (lowest_unset_bit >> 1))
    else:
        return x ^ (lowest_set_bit | (lowest_set_bit >> 1))
