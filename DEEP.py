from BFS import neighbors, is_goal
import time
import rank, unrank, read

def DEEP(start, goal, cycle_detection=True, verbose=False):
    max_length = 0
    frontier = []
    while True:
        if not frontier:
            max_length += 1
            frontier.append([start])
        path = frontier.pop() #select and remove last path from frontier
        last_vertex = path[-1]
        if is_goal(last_vertex, goal):  #check if last vertex in path is goal
            if verbose: #if asked by user, print each vertex(matrix) in path
                for matrices in path:
                    for line in matrices:
                        print(line)
                    print()
            print(len(path))    #print length of solution for convenience
            return path
        if len(path) == max_length:
            continue
        for next_vertex in neighbors(last_vertex):
            if cycle_detection:
                if next_vertex in path:
                    continue
            new_path = path + [next_vertex]
            frontier.append(new_path)
    return None

def DEEP2(start, goal, cycle_detection=True, verbose=False):
    bases, _, patterns, columns = rank.get_information(start) #parameters for unrank

    max_length = 0
    frontier = []
    start_int = rank.rank(start) #convert start matrix to its rank integer

    while True:
        if not frontier:
            max_length += 1
            frontier.append([start_int])
        path = frontier.pop()
        last_vertex = path[-1]

        # convert to matrix for goal and neighbors
        matrix_last = unrank.unrank(last_vertex, bases, patterns, columns)
        if is_goal(matrix_last, goal):
            if verbose: #if asked by user, print path
                print(path)
            print(len(path))
            return path
        if len(path) == max_length:
            continue
        for next_vertex in neighbors(matrix_last):
            int_next = rank.rank(next_vertex) #convert neighbor matrix to integer
            if cycle_detection:
                if int_next in path:
                    continue
            new_path = path + [int_next]
            frontier.append(new_path)
    return None

if __name__ == '__main__':
    start_time = time.time()

    '''
    testing cases
    '''
    # test_matrix, exit_row = [[1,1,0,1,1,0], [0,1,1,2,0,0], [0,1,1,0,1,0,]], 2
    # test_matrix, exit_row = [[2,0,1],[0,1,0], [1,0,0]], 2
    # test_matrix, exit_row = [[2,1,1,0], [0,1,0,0], [1,1,0,0]], 2
    test_matrix, exit_row = read.read('encoding.txt')
    path  = DEEP2(test_matrix, exit_row)

    if path == None:
        print("No solution was found")

    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence
