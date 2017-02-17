import numpy

def swap(x,y):
    return y,x

def rotate(matrix, row_idx, side):
    if side == "right":
        temp = list(matrix[row_idx])
        matrix[row_idx][0] = 0
        for i in range(1, len(temp)):
            matrix[row_idx][i] = temp[i-1]
    elif side == "left":
        temp = list(matrix[row_idx])
        matrix[row_idx][-1] = 0
        for i in range(0, len(temp)-1):
            matrix[row_idx][i] = temp[i+1]
    return(matrix)

def right(matrix_in):
    for j, row in enumerate(matrix_in):
        for k, value in enumerate(row):
            if value != 2:  #loop until you find 2
                 continue
            elif k == len(row)-1:
                return matrix_in
            elif matrix_in[j][k+1] == 0: #swap (move into blank space)
                matrix_in[j][k+1], matrix_in[j][k] = matrix_in[j][k], matrix_in[j][k+1]
                return matrix_in
            elif matrix_in[j][-1] != 0: #no possible movement to left
                return matrix_in
            elif matrix_in[j][k+1] == 1: #rotate left (push block chunk to left)
                return rotate(matrix_in, j, "right")
    return matrix_in

def left(matrix_in):
    for j, row in enumerate(matrix_in):
        for k, value in enumerate(row):
            if value != 2:
                 continue
            elif k == 0:
                return matrix_in
            elif matrix_in[j][k-1] == 0: #swap
                matrix_in[j][k-1], matrix_in[j][k] = matrix_in[j][k], matrix_in[j][k-1]
                return matrix_in
            elif matrix_in[j][0] != 0: #no possible movement to right
                return matrix_in
            elif matrix_in[j][k-1] == 1: #rotate right
                return rotate(matrix_in, j, "left")
    return matrix_in

def up(matrix_in):
    for j, row in enumerate(matrix_in):
        for k, value in enumerate(row):
            if value != 2:
                continue
            if j == 0:  #at border, no possible movement
                return matrix_in
            elif matrix_in[j-1][k] != 0: #block ahead, cannot move up
                return matrix_in
            else: #swap with blank space above
                matrix_in[j][k],matrix_in[j-1][k] = matrix_in[j-1][k], matrix_in[j][k]
                return matrix_in
    return matrix_in

def down(matrix_in):
    for j, row in enumerate(matrix_in):
        for k, value in enumerate(row):
            if value != 2:
                continue
            if j == len(matrix_in)-1:  #at border, no possible movement
                return matrix_in
            elif matrix_in[j+1][k] != 0: #block ahead, cannot move up
                return matrix_in
            else: #swap with blank space below
                matrix_in[j][k],matrix_in[j+1][k] = matrix_in[j+1][k], matrix_in[j][k]
                return matrix_in
    return matrix_in





test_matrix = [[0,0,1,1,1,0], [0,1,0,2,1,0], [0,1,1,0,1,0,]]
print("orig:\n", numpy.matrix(test_matrix),"\n")
print("down:\n",numpy.matrix(down(test_matrix)))
print("right:\n",numpy.matrix(right(test_matrix)))
print("up:\n",numpy.matrix(up(test_matrix)))
print("right:\n",numpy.matrix(left(test_matrix)))
