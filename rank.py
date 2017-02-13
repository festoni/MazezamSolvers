import numpy
from read import read

def rank(matrix_in):

    bases_arr = []
    digits_arr = []

    #Count the number of zeros strarting from left up to the leftmost 1 and
    #the number of zeros starting from the right up to the rightmost 1 for each
    #row, to determine the bases of these rows. Also, take note of the index
    #of the leftmost 1 in each row to determine its digit
    for row in matrix_in:
        base_count = 1;
        for index, val in enumerate(row):
            if val == 1:
                digits_arr.append(index)
                break
            base_count += 1
        for val in list(reversed(row)):
            if val == 1: break
            base_count += 1
        bases_arr.append(base_count)

    #counts all the 0s and the 2 in the matrix, these are the possible locations
    #and the current location of the player and give the base for the player
    #row in our representation; takes note at which of these locations is the
    #number 2 in, to get the digit for the player row,
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

    #convert the mixed-radix number to base 10 integer
    #calculates by looping through each element in digits array, it takes the
    #value of the current element on digits array, and multiplies it by
    #all the elements on the base array, starting at index+1
    #(index being that of current digit); for each item in the digits array, the
    #products are added together and the result is the integer in base 10
    unique_int = 0
    for index, digit in enumerate(digits_arr):
        temp_sum = digit
        for base in bases_arr[index+1:len(bases_arr)]:
            temp_sum *= base
        unique_int += temp_sum

    print("\nbases:\t", bases_arr)
    print("digits:\t", digits_arr)
    print("integer:",unique_int,"\n")
    
    return unique_int

def main():
    # matrix3 = [[2,1,1,0,0,1,1], [1,0,1,0,1,0,0], [0,0,0,1,1,0,1]]
    test_matrix2 = read('encoding.txt')
    rank(test_matrix2)

if __name__ == '__main__':
    main()
