import mechanics, read, rank, unrank #my functions
import copy
import time, numpy

#determine all possible movements of the player and return them as a list
def neighbors(vertex_m, with_cost=False):
    neighbors = []
    moves = mechanics.valid_moves(vertex_m)
    if "right" in moves:
        temp = copy.deepcopy(vertex_m)
        if with_cost == False:
            neighbors.append(mechanics.right(temp))
        else:
            neighbors.append(mechanics.right(temp, with_cost=True))
        moves.pop(0)
    if "left" in moves:
        temp = copy.deepcopy(vertex_m)
        if with_cost == False:
            neighbors.append(mechanics.left(temp))
        else:
            neighbors.append(mechanics.left(temp, with_cost=True))
        moves.pop(0)
    if "up" in moves:
        temp = copy.deepcopy(vertex_m)
        if with_cost == False:
            neighbors.append(mechanics.up(temp))
        else:
            neighbors.append(mechanics.up(temp, with_cost=True))
        moves.pop(0)
    if "down" in moves:
        temp = copy.deepcopy(vertex_m)
        if with_cost == False:
            neighbors.append(mechanics.down(temp))
        else:
            neighbors.append(mechanics.down(temp, with_cost=True))
        moves.pop(0)
    return neighbors

#check if given vertex is goal vertex
def is_goal(vertex, goal):
    if vertex[goal][-1] == 2:
        return True
    return False


def BFS(start, goal, cycle_detection=False, verbose=False):
    frontier = []
    frontier.append([start])
    while frontier:
        path = frontier.pop(0) #select and remove first path from frontier
        last_vertex = path[-1]
        if is_goal(last_vertex, goal):  #check if last vertex in path is goal
            if verbose: #if asked by user, print each vertex(matrix) in path
                for matrices in path:
                    for line in matrices:
                        print(line)
                    print()
            print("length:", len(path))    #print length of solution for convenience
            return path
        for next_vertex in neighbors(last_vertex):
            if cycle_detection:    #include cycle detection if asked for
                if next_vertex in path:
                    continue
            new_path = path + [next_vertex]
            frontier.append(new_path)
    return None

def BFS2(start, goal, cycle_detection=False, verbose=False):
    bases, _, patterns, columns = rank.get_information(start) #parameters for unrank
    frontier = []
    start_int = rank.rank(start) #convert start matrix to its rank integer
    frontier.append([start_int])

    #figure out size of visited array (by multiplying bases) and initialize it
    prod = 1
    for i in bases:
        prod *= i
    visited = [False for u in range(prod)]
    visited[start_int] = True

    while frontier:
        path = frontier.pop(0)
        last_vertex = path[-1]

        # convert from integer to matrix to check if goal and/or find neighbors
        matrix_last = unrank.unrank(last_vertex, bases, patterns, columns)
        if is_goal(matrix_last, goal):
            if verbose: #if asked by user, print path
                print(path)
            print("length:", len(path))
            return path
        for next_vertex in neighbors(matrix_last):
            int_next = rank.rank(next_vertex) #convert neighbor matrix to integer
            if cycle_detection:
                if visited[int_next]:
                    continue
            new_path = path + [int_next]
            visited[int_next] = True
            frontier.append(new_path)
    return None

if __name__ == '__main__':
    start_time = time.time()    #start keeping track of time

    '''
    testing cases
    '''
    # test_matrix, exit_row = [[1,1,0,1,1,0], [0,1,1,2,0,0], [0,1,1,0,1,0,], ], 2
    test_matrix, exit_row = read.read('encoding2.txt')
    # test_matrix, exit_row = [[2,1,1,0], [0,1,0,0], [1,1,0,0]], 2
    # test_matrix, exit_row = [[2,0,1],[0,1,0], [1,0,0]], 2
    path = BFS(test_matrix, exit_row, True, False)

    if path == None:
        print("No solution was found")

    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence
