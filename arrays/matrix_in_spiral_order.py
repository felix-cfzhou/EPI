# 4 pass solution O(n^2) time
def matrix_in_spiral_order(square_matrix):
    spiral_ordering = []
    def matrix_layer_in_clockwise(offset):
        if offset == len(square_matrix) - offset - 1:
            spiral_ordering.append(square_matrix[offset][offset])
            return
        spiral_ordering.extend(square_matrix[offset][offset:-1-offset])
        spiral_ordering.extend(square_matrix[offset:-1-offset][-1-offset])
        spiral_ordering.extend(square_matrix[-1-offset][-1-offset:offset:-1])
        spiral_ordering.extend(square_matrix[-1-offset:offset:-1][offset])
    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise(offset)
    return spiral_ordering


# One pass solution O(n^2) time
def matrix_in_spiral_order(square_matrix):
    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    spiral_ordering = []

    for _ in range(len(square_matrix)**2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x+SHIFT[direction][0], y+SHIFT[direction][1]
        if (next_x not in range(len(square_matrix))
                or next_y not in range(len(square_matrix))
                or square_matrix[next_x][next_y] == 0):
            direction = (direction+1) & 3  # equivalent to mod 3
            next_x, next_y = x+SHIFT[direction][0], y+SHIFT[direction][1]
        x, y = next_x, next_y
    return spiral_ordering
