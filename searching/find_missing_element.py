def find_missing_element(stream):
    NUM_BUCKET = 1 << 16
    counter = [0] * NUM_BUCKET
    stream, stream_copy = itertools.tee(stream)
    for x in stream:
        upper_part_x = x >> 16
        counter[upper_part_x] += 1

    BUCKET_CAPACITY = 1 << 16
    candidate_bucket = next(i for i, c in enumerate(counter) if c < BUCKET_CAPACITY)  # retrieves first one

    candidates = [0] * BUCKET_CAPACITY
    stream = stream_copy
    for x in stream_copy:
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            lower_part_x = ((1 << 16) - 1) & x  # extracts lower 16 bits
            candidates[lower_part_x] = 1

    for i, v in enumerate(candidates):
        if v == 0:  # find first non-existent one and return it
            return (candidate_bucket << 16) | i
