# O(n^2) solution
def is_valid_sudoku(partial_assignment):
    def has_duplicate(block):
        block = list(filter(lambda x: x!=0, block))
        return len(block) != len(set(block))

    N = len(partial_assignment)
    if any(
            has_duplicate([partial_assignment[i][j]
                for j in range(N)])
            or has_duplicate([partial_assignment[j][i]
                for j in range(N)])
                    for i in range(N)):
        return False

    region_size = int(math.sqrt(N))
    return all(
            not has_duplicate([partial_assignment[a][b]
                for a in range(region_size*I, region_size*J)
                for b in range(region_size*J, region_size*I)])
                    for I in range(region_size)
                    for J in range(region_size))


# more pythonic
def is_valid_sudoku(partial_assignment):
    region_size = int(math.sqrt(len(partial_assignment)))
    return max(
            collections.Counter(
                k
                    for i, row in enumerate(partial_assignment)
                    for j, c in enumerate(row)
                    if c != 0
                        for k in (
                            (i, str(c)),
                            (str(c), j),
                            (i//region_size, j//region_size, str(c)))).values(),
                default=0) <= 1
