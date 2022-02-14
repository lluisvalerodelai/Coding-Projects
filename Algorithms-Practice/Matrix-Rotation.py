#this is just some practice I was doing to work on my skills with 2d arrays. 
#any improvements are welcome, the more my skills and work improve, the better.


import numpy as np
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
matrix2 = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

def rotateMatrix(matrix):
    assert matrix.shape[0]/matrix.shape[1] == 1
    matrix = np.array(matrix)
    shape = matrix.shape
    flipped_matrix = np.zeros(shape, int)
    row_var = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if row_var == matrix.shape[0] and row_var == matrix.shape[1]:
                row_var = 0
            if i == 0:
                flipped_matrix[row_var][-1] = matrix[i][j]
                row_var += 1
            elif i == 1:
                flipped_matrix[row_var][-2] = matrix[i][j]
                row_var += 1
            else:
                flipped_matrix[row_var][-3] = matrix[i][j]
                row_var += 1 
    return flipped_matrix


print(f"original matrix is \n {matrix}")
print(f"rotated matrix is \n {rotateMatrix(matrix)}")
