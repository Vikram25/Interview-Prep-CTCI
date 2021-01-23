'''
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0. 
'''
#ref: https://github.com/careercup/CtCI-6th-Edition-Python/blob/e6bc732588601d0a98e5b1bc44d83644b910978d/Chapter1/
def zeroMatrix(matrix):
    row_zero = False
    col_zero = False
    
    for j in range(len(matrix[0])):
        if matrix[0][j] is 0:
            row_zero = True
            break
    
    for i in range(len(matrix)):
        if matrix[i][0] is 0:
            col_zero = True
            break
            
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] is 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    for i in range(1, len(matrix)):
        if matrix[i][0] is 0:
            nullify_row(matrix, i)
            
    for j in range(1, len(matrix[0])):
        if matrix[0][j] is 0:
            nullify_column(matrix, j)
    
    if row_zero:
        nullify_row(matrix, 0)
        
    if col_zero:
        nullify_column(matrix, 0)
        
    return matrix
            
def nullify_row(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0;
        
def nullify_column(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0;

mat1 = [[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]
print(zeroMatrix(mat1))
