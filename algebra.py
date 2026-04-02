def matrix_addition(A, B):
    """Adds two matrices of the same dimensions elementwise"""
    
    # Zip each row and add corresponding elements
    sum_matrix = [
        [a + b for a, b in zip(row_A, row_B)] 
        for row_A, row_B in zip(A, B)
        ]

    return sum_matrix


def matrix_subtraction(A, B):
    """Subtracts matrix B from matrix A elementwise"""

    # Zip each row and subtract corresponding elements
    diff_matrix = [
        [a - b for a, b in zip(row_A, row_B)] 
        for row_A, row_B in zip(A, B)
        ]

    return diff_matrix


def matrix_multiplication(A, B):
    """Returns matrix multiplication of matrix A with matrix B"""
    pass

def matrix_transpose(A):
    """Transposes matrix A"""

    # Swap the row and column indices for each element
    trans_matrix = [
        [A[i][i_row] for i, a in enumerate(row)]
        for i_row, row in enumerate(A)
    ]

    return trans_matrix

def scalar_multiplication(A, k):
    """Multiplies every value of matrix A by value k"""

    # Multiply each element by factor k
    factor_matrix = [
        [a * k for a in row]
        for row in A
    ]
            
    return factor_matrix