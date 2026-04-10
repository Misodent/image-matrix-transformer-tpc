# image transformation functions
from algebra import (matrix_addition, matrix_subtraction, matrix_multiplication, 
matrix_transpose, scalar_multiplication)
from misc_math import avg_luminosity

def image_to_matrix(image):
    pass

def matrix_to_image(matrix_red, matrix_green, matrix_blue):
    pass

def rotate_matrix(matrix, point, angle_degrees):
    pass

def scale_matrix(matrix, scale_factor):
    pass

def skew_matrix(matrix, skew_x, skew_y):
    pass

def transpose_matrix(matrix):
    """Transpose the matrix (Swap rows and columns)"""
    return matrix_transpose(matrix)

def to_grayscale(matrix_red, matrix_green, matrix_blue):
    """Returns single grayscale matrix based on input channels"""
    grayscale_matrix = [
        [avg_luminosity(r, g, b) for r, g, b in zip(r_row, g_row, b_row)]
        for r_row, g_row, b_row in zip(matrix_red, matrix_green, matrix_blue)
    ]

    return grayscale_matrix

def edge_detection(matrix):
    pass