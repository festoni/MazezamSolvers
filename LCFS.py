from BFS import neighbors, is_goal
import time, heapq
import rank, unrank, read

def LCFS(start, goal, cycle_detect=False, verbose=False):

    #frontier will look like [(cost, [path]), (cost, [path]), (cost, [path]),...]
    frontier = []   #this frontier will be used as a heap
    heapq.heappush(frontier, (0,[start]))   #heap prioritized by first element of tuple

    while frontier:

        #path_tuple = (cost, [path])
        path_tuple = heapq.heappop(frontier) #select and remove first path tuple from frontier

        #last_vertex = path[-1] from path_tuple
        last_vertex = path_tuple[1][-1]
        if is_goal(last_vertex, goal):  #check if last vertex in path is goal
            if verbose: #if asked by user, print each vertex(matrix) in path
                for matrices in path_tuple[1]:
                    for line in matrices:
                        print(line)
                    print()
            print("cost\t:", path_tuple[0])         #print cost of soln for convenience
            print("length\t:",len(path_tuple[1]))   #print length of solution for convenience
            return path_tuple
        for next_tuple in neighbors(last_vertex, with_cost=True):
            if cycle_detect:    #include cycle detection if asked for
                if next_tuple[1] in path_tuple[1]:
                    continue
            new_path = (path_tuple[0] + next_tuple[0], path_tuple[1] + [next_tuple[1]])
            heapq.heappush(frontier, new_path)
    return None


def LCFS2(start, goal, pruning=True, verbose=False):
    bases, _, patterns, columns = rank.get_information(start) #parameters for unrank
    start_int = rank.rank(start) #convert start matrix to its rank integer

    #frontier will look like [(cost, [path]), (cost, [path]), (cost, [path]),...]
    frontier = []   #this frontier will be used as a heap
    heapq.heappush(frontier, (0,[start_int]))   #heap prioritized by first element of tuple

    #figure out size of visited array (by multiplying bases) and initialize it
    prod = 1
    for i in bases:
        prod *= i
    visited = [False for u in range(prod)]
    visited[start_int] = True

    while frontier:
        #path_tuple = (cost, [path])
        path_tuple = heapq.heappop(frontier) #select and remove first path tuple from frontier

        #last_vertex = path[-1] from path_tuple
        last_vertex = path_tuple[1][-1]

        # convert from integer to matrix to check if goal and/or find neighbors
        matrix_last = unrank.unrank(last_vertex, bases, patterns, columns)
        if is_goal(matrix_last, goal):  #check if last vertex in path is goal
            if verbose: #if asked by user, print each vertex(matrix) in path
                print(path_tuple[1])
            print("cost\t:", path_tuple[0])         #print cost of soln for convenience
            print("length\t:",len(path_tuple[1]))   #print length of solution for convenience
            return path_tuple
        for next_tuple in neighbors(matrix_last, with_cost=True):
            int_next = rank.rank(next_tuple[1])
            if pruning:    #include cycle detection if asked for
                if visited[int_next]:
                    continue
            new_path = (path_tuple[0] + next_tuple[0], path_tuple[1] + [int_next])
            visited[int_next] = True
            heapq.heappush(frontier, new_path)
    return None


if __name__ == '__main__':
    start_time = time.time()    #start keeping track of time

    '''
    testing cases
    '''

    # test_matrix, exit_row = [[1,1,0,1,1,0], [0,1,1,2,0,0], [0,1,1,0,1,0,]], 2
    test_matrix, exit_row = read.read('encoding.txt')
    # test_matrix, exit_row = [[2,1,1,0], [0,1,0,0], [1,1,0,0]], 2

    path = LCFS2(test_matrix, exit_row, True, False)


    if path == None:
        print("No solution was found")
    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence
