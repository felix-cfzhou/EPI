def levenshtein_distance(A, B):
    def compute_distance_between_prefixes(A_idx, B_idx):
        if A_idx < 0:
            return B_idx + 1
        elif B_idx < 0:
            return A_idx + 1
        elif distance_between_prefixes[A_idx][B_idx] == -1:
            if A[A_idx] == B[B_idx]:
                distance_between_prefixes[A_idx][B_idx] = compute_distance_between_prefixes(A_idx-1, B_idx-1)
            else:
                substitute_last = compute_distance_between_prefixes(A_idx-1, B_idx-1)
                delete_last = compute_distance_between_prefixes(A_idx-1, B_idx)
                add_last = compute_distance_between_prefixes(A_idx, B_idx-1)
                distance_between_prefixes[A_idx][B_idx] = 1 + min(substitute_last, add_last, delete_last)
        return distance_between_prefixes[A_idx][B_idx]

    distance_between_prefixes=[[-1]*len(B) for _ in A]
    return compute_distance_between_prefixes(len(A)-1, len(B)-1)
