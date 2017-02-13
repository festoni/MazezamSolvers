import numpy
from read import read

def rank(matrix_in):

    bases_arr = []
    digits_arr = []
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

    print(bases_arr)
    print(digits_arr)

    unique_int = 0
    for index, digit in enumerate(digits_arr):
        temp_sum = digit
        for base in bases_arr[index+1:len(bases_arr)]:
            temp_sum *= base
        unique_int += temp_sum
    return unique_int



matrix3 = read('encoding.txt')
print()
rank(matrix3)

# print(numpy.matrix(matrix3))
