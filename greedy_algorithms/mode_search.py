def majority_search(input_stream):
    candidate, candidate_count = None, 0
    for it in input_stream:
        if candidate_count == 0:
            candidate, candidate_count = it, 1
        elif candidate == it:
            candidate_count += 1
        else:
            candidate_count -= 1
    return candidate
