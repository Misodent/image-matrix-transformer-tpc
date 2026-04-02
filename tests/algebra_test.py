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

def test_matrix_addition_1():
    sum_matrix = [
        [10, 10, 10],
        [10, 10, 10],
        [10, 10, 10]
    ]

    assert matrix_addition(matrix_A, matrix_B) == sum_matrix

def test_matrix_subtraction_1():
    diff_matrix = [
        [-8, -6, -4],
        [-2, 0, 2],
        [4, 6, 8]
    ]

    assert matrix_subtraction(matrix_A, matrix_B) == diff_matrix

def test_matrix_multiplication_1():
    mult_matrix = [
        [30, 24, 18],
        [84, 69, 54],
        [138, 114, 90]
    ]

    assert matrix_multiplication(matrix_A, matrix_B) == mult_matrix

def test_matrix_transpose_1():
    trans_matrix = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]

    assert matrix_transpose(matrix_A) == trans_matrix

def test_scalar_multiplication_1():
    prod_matrix = [
        [2, 4, 6],
        [8, 10, 12],
        [14, 16, 18]
    ]

    assert scalar_multiplication(matrix_A, 2) == prod_matrix