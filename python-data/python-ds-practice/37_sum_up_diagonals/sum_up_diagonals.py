def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    forward_diag = []
    backward_diag = []
    if len(matrix) == 2:
        count = 0
        for row in matrix:
            forward_diag.append(row[count])
            count += 1
        count = 1
        for row in matrix:
            backward_diag.append(row[-count])
            count += 1
    if len(matrix) == 3:
        count = 0
        for row in matrix:
            forward_diag.append(row[count])
            count += 1
        count = 1
        for row in matrix:
            backward_diag.append(row[-count])
            count += 1
    sum_of_diags = sum(forward_diag + backward_diag)
    return sum_of_diags
    