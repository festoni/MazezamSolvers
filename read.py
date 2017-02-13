import numpy

# see below the comment for the main loop for information on how this function works
def read(in_file):
    # read and enter the input file contents into a string
    input_file = open(in_file, 'r')
    input_string = input_file.read()


    # Calculates the dimensions of the matrix.
    # Figures out number of columns by iterating the first line of
    # hashtags, while keeping count and finally subtracting 6, for the initial
    # and ending 3 hashtags that are not part of the area of interest.
    # Figures out number of rows by counting the number of newlines \n and subtracting
    # 2 for the top and bottom lines which are not in area of interest
    columns = 0
    rows = 0
    for i in input_string:  #iterate the first line of hashtags to determine matrix size
        if i == '\n':       #once you hit end of line stop counting
            break
        columns += 1
    columns -= 6            #subtract the six hashtags not in area of interest

    for i in input_string:
        if i == '\n':
            rows += 1
    rows -= 2               #subtract top and bottom hashtags not in area of interest

    # initialize the matrix with figured out dimensions
    matrix = [[0 for j in range(columns)] for k in range(rows)]

    # this loop iterates the string and updates matrix entries as required
    # the overall way this loop works is by keeping a pointer the current matrix
    # entry (j, k) which needs to be updated. It starts at (0,0) and only updates
    # the value at that entry and the entry itself when an area of interest
    # character is being looked at. So characters like '#', '\n', 'P' are not
    # area of interest characters. DOT characters '.' OUTSIDE of area of interest are skipped.
    # When '.'is INSIDE area of interest, then it only updates the pointer (j, k)
    # to (j, k+1) and not values because matrix was already initialized to all zeros.
    # The characters '+' and '*' update the matrix entry being pointed at AND
    # the pointer, however characters that follow or precede, respectively,
    # check to make sure they don't mistakingly and wrongly update the pointer again
    # The rest of characters 'L', 'C', and 'R', update both the matrix entry and
    # the pointer.
    j, k = 0, 0
    for index, u in enumerate(input_string):
        if u == '#' or u == '\n':
            #if hashtag is preceded by area of interest character set index to next row of matrix
            if input_string[index-1] != '#' and input_string[index-1] != '\n':
                j += 1
                k = 0
            continue
        elif u == 'L' or u == 'C' or u == 'R': #enter 1 in matrix, set index to next column
            matrix[j][k] = 1
            k += 1

            #make sure not to update pointer, if it was already done so by the preceding '+'
            #this might never occur in the game, because usually right after the
            #entry gate there is a blank space. If, however, on later levels there is
            #a movable block right after the enter gate, this takes care of it
            if input_string[index-1] == '+':
                continue

            continue
        elif u == '.':    #if DOT is in area of interest, update column index, otherwise skip
            if input_string[index+1] == '+' or input_string[index+1] == 'X':
                continue
            if input_string[index-1] == '+':
                continue #make sure not to update pointer, if it was already done so by the preceding '+'
            k += 1
            continue
        elif u == '+':  #if you run into the +, set matrix value to 2
            matrix[j][k] = 2
            k += 1
            continue
        elif u == '*':  #if you run into #, set matrix entry to 9
            matrix[j][k-1] = 0
            k = 0
            continue
        else:
            continue
    return matrix

def main():
    test_matrix = read('encoding.txt')
    print("\n", numpy.matrix(test_matrix), "\n")

if __name__ == '__main__':
    main()
