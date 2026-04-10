import pytest

from algebra import matrix_addition, matrix_subtraction, matrix_transpose, matrix_multiplication, scalar_multiplication
from misc_math import column

matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

matrix_C = [
    [12, 11, 10],
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

matrix_4x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

matrix_3x2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

matrix_2x3 = [
    [1, 2, 3],
    [4, 5, 6]
]

def test_matrix_addition_1():
    sum_matrix = [
        [10, 10, 10],
        [10, 10, 10],
        [10, 10, 10]
    ]

    assert matrix_addition(matrix_A, matrix_B) == sum_matrix

def test_matrix_addition_2():
    sum_matrix = [
        [13, 13, 13],
        [13, 13, 13],
        [13, 13, 13],
        [13, 13, 13]
    ]

    assert matrix_addition(matrix_C, matrix_4x3) == sum_matrix

def test_matrix_addition_invalid_dimensions():
    test_passed = False
    
    try:
        matrix_addition(matrix_A, matrix_4x3)
    except ValueError:
        test_passed = True

    assert test_passed

def test_matrix_subtraction_1():
    diff_matrix = [
        [-8, -6, -4],
        [-2, 0, 2],
        [4, 6, 8]
    ]

    assert matrix_subtraction(matrix_A, matrix_B) == diff_matrix

def test_matrix_subtraction_2():
    diff_matrix = [
        [-11, -9, -7],
        [-5, -3, -1],
        [1, 3, 5],
        [7, 9, 11]
    ]

    assert matrix_subtraction(matrix_4x3, matrix_C) == diff_matrix

def test_matrix_substraction_invalid_dimensions():
    test_passed = False

    try:
        matrix_subtraction(matrix_A, matrix_4x3)
    except ValueError:
        test_passed = True

    assert test_passed


def test_matrix_multiplication_1():
    mult_matrix = [
        [30, 24, 18],
        [84, 69, 54],
        [138, 114, 90]
    ]

    assert matrix_multiplication(matrix_A, matrix_B) == mult_matrix

def test_matrix_multiplication_2():
    mult_matrix = [
        [22, 28],
        [49, 64],
        [76, 100],
        [103, 136]
    ]

    assert matrix_multiplication(matrix_4x3, matrix_3x2) == mult_matrix

def test_matrix_multiplication_invalid_dimensions_1():
    test_passed = False

    try:
        matrix_multiplication(matrix_2x3, matrix_4x3)
    except ValueError:
        test_passed = True
    
    assert test_passed

def test_matrix_multiplication_invalid_dimensions_2():
    test_passed = False

    try:
        matrix_multiplication(matrix_3x2, matrix_4x3)
    except ValueError:
        test_passed = True
    
    assert test_passed

def test_matrix_multiplication_invalid_dimensions_3():
    test_passed = False

    try:
        matrix_multiplication(matrix_3x2, matrix_A)
    except ValueError:
        test_passed = True
    
    assert test_passed

def test_matrix_multiplication_invalid_dimensions_4():
    test_passed = False

    try:
        matrix_multiplication(matrix_A, matrix_4x3)
    except ValueError:
        test_passed = True
    
    assert test_passed

def test_matrix_transpose_1():
    trans_matrix = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]

    assert matrix_transpose(matrix_A) == trans_matrix

def test_matrix_transpose_2():
    trans_matrix = [
        [12, 9, 6, 3],
        [11, 8, 5, 2],
        [10, 7, 4, 1],
    ]

    assert matrix_transpose(matrix_C) == trans_matrix


def test_scalar_multiplication_1():
    prod_matrix = [
        [2, 4, 6],
        [8, 10, 12],
        [14, 16, 18]
    ]

    assert scalar_multiplication(matrix_A, 2) == prod_matrix

def test_scalar_multiplication_2():
    prod_matrix = [
        [24, 22, 20],
        [18, 16, 14],
        [12, 10, 8],
        [6, 4, 2]
    ]

    assert scalar_multiplication(matrix_C, 2) == prod_matrix