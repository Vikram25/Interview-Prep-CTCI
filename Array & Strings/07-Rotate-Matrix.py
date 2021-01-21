'''
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
'''
#ref: https://github.com/careercup/CtCI-6th-Edition-Python/blob/e6bc732588601d0a98e5b1bc44d83644b910978d/Chapter1/7_Rotate%20Matrix/RotateMatrix.py


def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]
            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]
            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]
            # top -> right
            matrix[i][- layer - 1] = top
    return matrix

matrix_1 = [ [1, 2, 3, 4], [3, 4, 5, 6] , [6, 7, 8, 9], [10, 11, 12, 13] ]
print(rotate_matrix(matrix_1))