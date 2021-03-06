'''
Write a function that accepts an integer N
and returns a NxN spiral matrix.
--- Examples
  matrix(2)
    [[1, 2],
    [4, 3]]
  matrix(3)
    [[1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]]
  matrix(4)
    [[1,  2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7]]
'''


def spiral_matrix(n):
    ''' returns a n * n spiral matrix.'''
    # initialise an empty matrix
    matrix = [[0 for i in range(n)] for j in range(n)]
    # declare vars used in iteration
    counter = 1
    start_row = 0
    start_col = 0
    end_row = n - 1
    end_col = n - 1

    while start_row <= end_row and start_col <= end_col:
        # current top row left-right
        for i in range(start_col, end_col + 1):
            matrix[start_row][i] = counter
            counter += 1
        start_row += 1

        # rightmost col top-down
        for i in range(start_row, end_row + 1):
            matrix[i][end_col] = counter
            counter += 1
        end_col -= 1

        # bottom row right-left
        for i in reversed(range(start_col, end_col + 1)):
            matrix[end_row][i] = counter
            counter += 1
        end_row -= 1

        # leftmost col down-top
        for i in reversed(range(start_row, end_row + 1)):
            matrix[i][start_col] = counter
            counter += 1
        start_col += 1

    return matrix
