import numpy

#find the player position (2) in matrix and return its indices
def player_pos(matrix):
    for j, row in enumerate(matrix):
        for k, entry in enumerate(row):
            if matrix[j][k] == 2:
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

#determine if a move to the right is possible
def can_right(matrix_in, j, k):
    if k == len(matrix_in[j])-1:  #already in rightmost position
        return False
    elif matrix_in[j][k+1] != 0 and matrix_in[j][-1] != 0: #no possible movement to right
        return False
    else:
        return True

#determine if a move to the left is possible
def can_left(matrix_in, j, k):
    if k == 0:  #already in leftmost position
        return False
    elif matrix_in[j][k-1] != 0 and matrix_in[j][0] != 0: #no possible movement to left
        return False
    else:
        return True

#determine if a move up is possible
def can_up(matrix_in, j, k):
    if j == 0:  #at border, no possible movement
        return False
    elif matrix_in[j-1][k] != 0: #block ahead, cannot move up
        return False
    else:
        return True

#determine if a move down is possible
def can_down(matrix_in, j, k):
    if j == len(matrix_in)-1:  #at border, no possible movement
        return False
    elif matrix_in[j+1][k] != 0: #block ahead, cannot move up
        return False
    else:
        return True

#calls all the "can_" functions and returns a list of possible moves
def valid_moves(matrix_in):
    j, k = player_pos(matrix_in)
    valid_moves = []
    if can_right(matrix_in, j, k):
        valid_moves.append("right")
    if can_left(matrix_in, j, k):
        valid_moves.append("left")
    if can_up(matrix_in, j, k):
        valid_moves.append("up")
    if can_down(matrix_in, j, k):
        valid_moves.append("down")
    return valid_moves

#move to the right (is and should only be called when a move to right is possible)
def right(matrix_in):
    j, k = player_pos(matrix_in)
    if matrix_in[j][k+1] == 0: #swap (move into blank space)
        matrix_in[j][k+1], matrix_in[j][k] = matrix_in[j][k], matrix_in[j][k+1]
        return matrix_in
    elif matrix_in[j][k+1] == 1: #rotate right (push block chunk to right)
        return rotate(matrix_in, j, "right")

#move to the left (is and should only be called when a move to left is possible)
def left(matrix_in):
    j, k = player_pos(matrix_in)
    if matrix_in[j][k-1] == 0: #swap
        matrix_in[j][k-1], matrix_in[j][k] = matrix_in[j][k], matrix_in[j][k-1]
        return matrix_in
    elif matrix_in[j][k-1] == 1: #rotate left
        return rotate(matrix_in, j, "left")

#move player up (is and should only be called when a move up is possible)
def up(matrix_in):
    j, k = player_pos(matrix_in)
    matrix_in[j][k],matrix_in[j-1][k] = matrix_in[j-1][k], matrix_in[j][k]
    return matrix_in

#move player down (is and should only be called when a move down is possible)
def down(matrix_in):
    j, k = player_pos(matrix_in)
    matrix_in[j][k],matrix_in[j+1][k] = matrix_in[j+1][k], matrix_in[j][k]
    return matrix_in

if __name__ == '__main__':
    test_matrix = [[1,1,0,1,1,0], [0,1,1,2,0,0], [0,1,1,0,1,0,]]

    #this showcases a single instance of all four moves
    print("orignal:\n", numpy.matrix(test_matrix),"\n")

    j, k = player_pos(test_matrix)
    if can_down(test_matrix, j, k):
        print("down:\n",numpy.matrix(down(test_matrix)))
    j, k = player_pos(test_matrix)
    if can_right(test_matrix, j, k):
        print("right:\n",numpy.matrix(right(test_matrix)))
    j, k = player_pos(test_matrix)
    if can_left(test_matrix, j, k):
        print("left:\n",numpy.matrix(left(test_matrix)))
    j, k = player_pos(test_matrix)
    if can_up(test_matrix, j, k):
        print("up:\n",numpy.matrix(up(test_matrix)))
