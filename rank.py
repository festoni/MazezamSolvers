import numpy
import read

'''
This function takes in a matrix and returns, the bases array, the digits array,
the block chunk patterns for each row, and the number of columns. The rank
function only requires the first two return values, however three of these
return values are required by the search functions whenever they have to call and
pass them as parameters for the unrank function.
'''
def get_information(matrix_in):
    bases_arr = []
    digits_arr = []
    patterns_arr = []
    columns = len(matrix_in[0])

    '''
    Count the number of zeros starting from left up to the leftmost 1 and
    the number of zeros starting from the right up to the rightmost 1 for each
    row, to determine the bases of these rows. Also, take note of the index
    of the leftmost 1 in each row to determine its digit
    Note: number of zeros on right of block chunk + number of zeros on left of block
    chunk + 1 (space already taken by the block chunk) equals the base of that row.
    '''
    for index, row in enumerate(matrix_in):
        s, f = 0, 0         #variables to track beginning and ending of block pattern
        base_count = 1;
        for idx, val in enumerate(row): #count zeros up to first 1 from left
            if val == 1:
                digits_arr.append(idx)
                s = idx         #record index at which block pattern starts
                break
            base_count += 1
        for idx, val in list(enumerate(reversed(row))): #count zeros up to first 1 from right
            if val == 1:
                f = len(row) - idx - 1  #record index at which block pattern ends
                break
            base_count += 1
        bases_arr.append(base_count)

        #record the patterns for each row and add them to patterns_arr
        temp_pattern = []
        for i in range(s, f+1):
            temp_pattern.append(matrix_in[index][i])
        patterns_arr.append(temp_pattern)

    '''
    counts all the 0s and the 2 in the matrix, these are the possible locations
    and the current location of the player and give the base for the player
    row in our representation; takes note at which of these locations is the
    number 2 in, to get the digit for the player row
    '''
    player_base = 0
    for row in matrix_in:
        for column in row:
            if column == 0:
                player_base += 1
            if column == 2:
                player_digit = player_base
                player_base += 1
    bases_arr.append(player_base)   #add player base to array of bases
    digits_arr.append(player_digit) #add player digit to array of digits
    return bases_arr, digits_arr, patterns_arr, columns


def rank(matrix_in):

    #see comments on get_bases_digits function
    bases_arr, digits_arr, _, _ = get_information(matrix_in)


    '''
    convert the mixed-radix number to base 10 integer:
    calculates by looping through each element in digits array, it takes the
    value of the current element on digits array, and multiplies it by
    all the elements on the base array, starting at index+1
    (index being that of current digit); for each item in the digits array, the
    products are added together and the result is the integer in base 10
    '''
    unique_int = 0
    for index, digit in enumerate(digits_arr):
        temp_sum = digit
        for base in bases_arr[index+1:len(bases_arr)]:
            temp_sum *= base
        unique_int += temp_sum

    return unique_int


if __name__ == '__main__':
    matrix3 = [[0,1,1,0,0,1,1], [1,0,1,0,1,0,0], [0,0,2,1,1,0,1]]
    # matrix3, exit = read.read('encoding.txt')
    print("\ninput matrix:\n", numpy.matrix(matrix3))
    integer = rank(matrix3)
    bases, digits, patterns, columns = get_information(matrix3)

    print("\nbases:\t", bases)
    print("digits:\t", digits)
    print("integer:",integer,"\n")
