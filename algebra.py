from misc_math import dot_product, column

def matrix_addition(A, B):
    """Adds two matrices of the same dimensions elementwise"""
    
    if (len(A) != len(B) or len(A[0]) != len(B[0])):
        raise ValueError("Matrix dimensions must match")
    
    # Zip each row and add corresponding elements
    sum_matrix = [
        [a + b for a, b in zip(row_A, row_B)] 
        for row_A, row_B in zip(A, B)
        ]

    return sum_matrix


def matrix_subtraction(A, B):
    """Subtracts matrix B from matrix A elementwise"""

    if (len(A) != len(B) or len(A[0]) != len(B[0])):
        raise ValueError("Matrix dimensions must match")

    # Zip each row and subtract corresponding elements
    diff_matrix = [
        [a - b for a, b in zip(row_A, row_B)] 
        for row_A, row_B in zip(A, B)
        ]

    return diff_matrix


def matrix_multiplication(A, B):
    """Returns matrix multiplication of matrix A with matrix B"""

    if (len(A[0]) != len(B)):
        raise ValueError("The number of collums in one matrix must match the number of rows in the other one")

    # Multiplied matrix will have dimensions of the smallest row and column length of the inputs
    min_column_length = min(len(A), len(B))
    min_row_length = min(len(A[0]), len(B[0]))
    
    # Initialise empty matrix to aforementioned dimensions
    mult_matrix = [
        [0 for i in range(min_row_length)]
        for i in range(min_column_length)
    ]

    for i_row, row in enumerate(A):
        for i_element, element in enumerate(B[i_row]):
            col = column(B, i_element)
            dot_prod = dot_product(row, col)

            mult_matrix[i_row][i_element] = dot_prod
            
    return mult_matrix


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