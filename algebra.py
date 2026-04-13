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
        raise ValueError("""The column length of matrix A must match the 
        row length of matrix B""")
    
    # Dot product of row and column for each resulting element
    return [
        [dot_product(row, column(B, j)) for j in range(len(B[0]))]
        for row in A
    ]


def matrix_transpose(A):
    """Transposes matrix A"""

    # Swap the row and column indices for each element
    trans_matrix = [
        [A[j][i] for j in range(len(A))]
        for i in range(len(A[0]))
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