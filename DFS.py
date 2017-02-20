from BFS import neighbors, is_goal
import time
import rank, unrank, read

def DFS(start, goal, verbose=False):
    frontier = []
    frontier.append([start])
    while frontier:
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
        for next_vertex in neighbors(last_vertex):
            new_path = path + [next_vertex]
            frontier.append(new_path)
    return None

def DFS_cycle(start, goal, verbose=False):
    frontier = []
    frontier.append([start])
    while frontier:
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
        for next_vertex in neighbors(last_vertex):
            if next_vertex in path:
                continue
            new_path = path + [next_vertex]
            frontier.append(new_path)
    return None

def DFS_prune(start, goal, verbose=False):
    frontier = []
    frontier.append([start])
    while frontier:
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

        in_path = False
        for next_vertex in neighbors(last_vertex):
            for item in frontier:
                if next_vertex in item:
                    # print("ever been here?")
                    in_path = True
                    continue
            if in_path:
                continue
            new_path = path + [next_vertex]
            frontier.append(new_path)
    return None

def DFS2(start, goal, verbose=False):
    bases, _, patterns, columns = rank.get_information(start) #parameters for unrank
    frontier = []
    start_int = rank.rank(start) #convert start matrix to its rank integer
    frontier.append([start_int])

    while frontier:
        path = frontier.pop()
        last_vertex = path[-1]

        # convert to matrix for goal and neighbors
        matrix_last = unrank.unrank(last_vertex, bases, patterns, columns)
        if is_goal(matrix_last, goal):
            if verbose: #if asked by user, print path
                print(path)
            print(len(path))
            return path
        for next_vertex in neighbors(matrix_last):
            int_next = rank.rank(next_vertex) #convert neighbor matrix to integer
            new_path = path + [int_next]
            frontier.append(new_path)
    return None

def DFS_cycle2(start, goal, verbose=False):
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
        path = frontier.pop()
        last_vertex = path[-1]

        # convert to matrix for goal and neighbors
        matrix_last = unrank.unrank(last_vertex, bases, patterns, columns)
        if is_goal(matrix_last, goal):
            if verbose: #if asked by user, print path
                print(path)
            print(len(path))
            return path
        for next_vertex in neighbors(matrix_last):
            int_next = rank.rank(next_vertex) #convert neighbor matrix to integer
            if visited[int_next]:
                continue
            new_path = path + [int_next]
            visited[int_next] = True
            frontier.append(new_path)
    return None

def DFS_prune2(start, goal, verbose=False):
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
        path = frontier.pop()
        last_vertex = path[-1]

        # convert to matrix for goal and neighbors
        matrix_last = unrank.unrank(last_vertex, bases, patterns, columns)
        if is_goal(matrix_last, goal):
            if verbose: #if asked by user, print path
                print(path)
            print(len(path))
            return path
        for next_vertex in neighbors(matrix_last):
            int_next = rank.rank(next_vertex) #convert neighbor matrix to integer
            if visited[int_next]:
                continue
            new_path = path + [int_next]
            visited[int_next] = True
            frontier.append(new_path)
    return None


if __name__ == '__main__':
    start_time = time.time()

    # test_matrix, exit_row = [[1,1,0,1,1,0], [0,1,1,2,0,0], [0,1,1,0,1,0,]], 2
    test_matrix, exit_row = [[2,0,1],[0,1,0], [1,0,0]], 2
    # test_matrix, exit_row = [[2,1,1,0], [0,1,0,0], [1,1,0,0]], 2
    # test_matrix, exit_row = read.read('encoding2.txt')
    path  = DFS_prune2(test_matrix, exit_row, False)

    if path == None:
        print("No solution was found")

    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence
