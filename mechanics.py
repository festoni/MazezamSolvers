import numpy

#find the player position (2) in matrix and return its indices
def player_pos(matrix):
    for j, row in enumerate(matrix):
        for k, entry in enumerate(row):
            if matrix[j][k] == 2:
                print("j is", j)
                print("k is", k)
                return j, k

#rotate the whole row to left/right, when player successfully pushes block chunk
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
    j, k = player_pos(matrix_in)
    if k == len(matrix_in[j])-1:  #already in rightmost position
        return None
    elif matrix_in[j][k+1] == 0: #swap (move into blank space)
        matrix_in[j][k+1], matrix_in[j][k] = matrix_in[j][k], matrix_in[j][k+1]
        return matrix_in
    elif matrix_in[j][-1] != 0: #no possible movement to right
        return None
    elif matrix_in[j][k+1] == 1: #rotate right (push block chunk to right)
        return rotate(matrix_in, j, "right")
    return None

def left(matrix_in):
    j, k = player_pos(matrix_in)
    if k == 0:  #already in leftmost position
        return None
    elif matrix_in[j][k-1] == 0: #swap
        matrix_in[j][k-1], matrix_in[j][k] = matrix_in[j][k], matrix_in[j][k-1]
        return matrix_in
    elif matrix_in[j][0] != 0: #no possible movement to left
        return None
    elif matrix_in[j][k-1] == 1: #rotate left
        return rotate(matrix_in, j, "left")
    return None

def up(matrix_in):
    j, k = player_pos(matrix_in)
    if j == 0:  #at border, no possible movement
        return None
    elif matrix_in[j-1][k] != 0: #block ahead, cannot move up
        return None
    else: #swap with blank space above
        matrix_in[j][k],matrix_in[j-1][k] = matrix_in[j-1][k], matrix_in[j][k]
        return matrix_in
    return None


def down(matrix_in):
    j, k = player_pos(matrix_in)
    if j == len(matrix_in)-1:  #at border, no possible movement
        return None
    elif matrix_in[j+1][k] != 0: #block ahead, cannot move up
        return None
    else: #swap with blank space below
        matrix_in[j][k],matrix_in[j+1][k] = matrix_in[j+1][k], matrix_in[j][k]
        return matrix_in
    return None

if __name__ == '__main__':

    test_matrix = [[1,1,1,0,2,1], [0,1,1,0,0,0], [0,1,1,0,1,0,]]
    print("orig:\n", numpy.matrix(test_matrix),"\n")
    print("down:\n",numpy.matrix(down(test_matrix)))
    print("right:\n",numpy.matrix(right(test_matrix)))
    print("up:\n",numpy.matrix(up(test_matrix)))
    print("left:\n",numpy.matrix(left(test_matrix)))
