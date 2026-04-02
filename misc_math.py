def dot_product(vector_A, vector_B):
    product = 0

    for a, b in zip(vector_A, vector_B):
        product += a * b

    return product

def column(matrix, i):
    column = []

    for row in matrix:
        column.append(row[i])

    return column
