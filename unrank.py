import numpy

'''
The function takes in the integer, the bases array, the block pattern, and the
number of columns that make up the level. The integer is what we are trying to
unrank from, the bases array will be used to get the digits array. The block patterns
are basically strings starting from the beginning of the block chunk all the way to
the end of the block chunk. It is called a pattern because it also describes the
blank spaces within the block chunk. And also how long individual block is in the
chunk. The block pattern in the matrix start at the digit-th column.
'''
def unrank(uniq_int, bases_arr, block_patterns, columns):

    '''
    This part figures out the digits array from the integer and the base array.
    It pops the first item from the base, then multiplies the remaining bases, and
    then does integer division of the integer and the product of remaining bases.
    The integer result is added on the digit array. Lastly, the integer is now
    updated to equal the remainder of itself divided by product of bases. This keeps
    going until there are no more elements left in the bases array
    '''
    temp_int = uniq_int
    digits_arr = []
    while len(bases_arr) != 0:  #run loop until no more elements in bases array
        bases_arr.pop(0)
        temp = 1
        for i in bases_arr:     #multiply all the current bases in the array
             temp *= i
        digit = temp_int // temp    #do integer division on integer and bases product
        if temp > temp_int:         #if bases product greater than integer, put 0 as digit
            digits_arr.append(0)
            temp_int = temp_int % temp
            continue
        digits_arr.append(digit)
        temp_int = temp_int % temp

    state_m = [[0 for j in range(columns)] for k in range(len(digits_arr)-1)]

    '''
    This part iterates the rows and the digits array. For every digit,
    it goes to that column in the row, and starts entering the corresponding
    block pattern that was given as input.
    '''
    for idx, digit in enumerate(digits_arr):
        if idx == len(digits_arr)-1:
            break
        row_patt = block_patterns[idx] #pick the pattern for the corresponding row
        j = digit                      #variable at which to start inserting the pattern
        for i in range(len(row_patt)):
            state_m[idx][j] = row_patt[i]
            j += 1

    '''
    This part iterates through all the zeros (blanks), and when it hits the
    player_digit-th zero it changes it into a 2.
    '''
    p = 0
    for row, val in enumerate(state_m):
        for column, val2 in enumerate(state_m[row]):
            if val2 != 0:
                continue
            if p == 9:
                state_m[row][column] = 2
                break                       #when you hit player position stop
            p += 1
        if p == 9:
            break                           #when you hit player position stop

    return state_m


if __name__ == '__main__':

    #testing
    integer = 174
    bases = [2, 3, 4, 11]
    block_pattern = [[1,1,0,0,1,1], [1,0,1,0,1], [1,1,0,1], [2]]
    num_columns = 7

    test_matrix = unrank(integer, bases, block_pattern, num_columns)
    print("\n",numpy.matrix(test_matrix),"\n")
