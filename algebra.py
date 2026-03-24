# linear algebra functions

def matrix_addition(A, B):
    """Adds two matrices of the same dimensions elementwise"""
    
    new_matrix = A 

    for i_row, row in enumerate(new_matrix):
        for i_column, element_A in enumerate(row):
            element_B = B[i_row][i_column]
            new_element = element_A + element_B

            row[i_column] = new_element

    return new_matrix


def matrix_subtraction(A, B):
    """Subtracts matrix B from matrix A elementwise"""

    new_matrix = A 

    for i_row, row in enumerate(new_matrix):
        for i_column, element_A in enumerate(row):
            element_B = B[i_row][i_column]
            new_element = element_A - element_B

            row[i_column] = new_element

    return new_matrix


def matrix_multiplication(A, B):
    """Returns cross product of matrix A with matrix B"""
    pass

def matrix_transpose(A):
    """Transposes matrix A"""
    new_matrix = A

    for i_row, row in enumerate(A):
        for i_column, element in enumerate(row):
            new_matrix[i_row][i_column] = A[i_column][i_row]
            new_matrix[i_column][i_row] = A[i_row][i_column]

    return new_matrix

def scalar_multiplication(A, k):
    """Multiplies every value of matrix A by value k"""

    new_matrix = A

    for i_row, row in enumerate(new_matrix):
        for i_column, element in enumerate(row):
            new_element = element * k
            
            row[i_column] = new_element
            
    return new_matrix