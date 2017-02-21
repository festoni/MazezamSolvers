from BFS import neighbors, is_goal
import mechanics, read, rank, unrank
import time, numpy

def BFS3(start, goal, cycle_detect=False, verbose=False, ranking=False):
    frontier = []

    if ranking:
        bases, _, patterns, columns = rank.get_information(start)
        start_int = rank.rank(start)
        frontier.append([start_int])

        #figure out size of visited array (by multiplying bases) and initialize it
        prod = 1
        for i in bases:
            prod *= i
        visited = [False for u in range(prod)]
        visited[start_int] = True
    else:
        frontier.append([start])

    while frontier:
        path = frontier.pop(0) #select and remove first path from frontier
        last_vertex = path[-1]

        if ranking:
            # convert from integer to matrix to check if goal and/or find neighbors
            last_vertex = unrank.unrank(last_vertex, bases, patterns, columns) ####!!!!!####

        if is_goal(last_vertex, goal):  #check if last vertex in path is goal
            if verbose: #if asked by user, print each vertex(matrix) in path
                if ranking:
                    print(path)
                else:
                    for matrices in path:
                        for line in matrices:
                            print(line)
                        print()
            print(len(path))    #print length of solution for convenience
            return path


        #enter procedure here, if user asked to use ranking/unranking
        if ranking:
            for next_vertex in neighbors(last_vertex):          ###!!!###
                int_next = rank.rank(next_vertex) #convert neighbor matrix to integer
                if cycle_detect:
                    if visited[int_next]:
                        continue
                new_path = path + [int_next]
                visited[int_next] = True
                frontier.append(new_path)

        #enter procedure here, if user did not want to use ranking/unranking
        else:
            for next_vertex in neighbors(last_vertex):
                if cycle_detect:    #include cycle detection if asked for
                    if next_vertex in path:
                        continue
                new_path = path + [next_vertex]
                frontier.append(new_path)

    return None

if __name__ == '__main__':
    start_time = time.time()    #start keeping track of time

    '''
    testing cases
    '''
    # test_matrix, exit_row = [[1,1,0,1,1,0], [0,1,1,2,0,0], [0,1,1,0,1,0,], ], 2
    test_matrix, exit_row = read.read('encoding.txt')
    # test_matrix, exit_row = [[2,1,1,0], [0,1,0,0], [1,1,0,0]], 2
    # test_matrix, exit_row = [[2,0,1],[0,1,0], [1,0,0]], 2
    path = BFS3(test_matrix, exit_row, True, False, True)

    if path == None:
        print("No solution was found")

    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence
