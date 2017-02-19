import mechanics
import numpy
import copy
import read
import time

#determine all possible movements of the player and return them as a list
def neighbors(vertex_m):
    neighbors = []
    moves = mechanics.valid_moves(vertex_m)
    if "right" in moves:
        temp = copy.deepcopy(vertex_m)
        neighbors.append(mechanics.right(temp))
        moves.pop(0)
    if "left" in moves:
        temp = copy.deepcopy(vertex_m)
        neighbors.append(mechanics.left(temp))
        moves.pop(0)
    if "up" in moves:
        temp = copy.deepcopy(vertex_m)
        neighbors.append(mechanics.up(temp))
        moves.pop(0)
    if "down" in moves:
        temp = copy.deepcopy(vertex_m)
        neighbors.append(mechanics.down(temp))
        moves.pop(0)
    return neighbors

#check if given vertex is goal vertex
def is_goal(vertex, goal):
    if vertex[goal][-1] == 2:
        return True
    return False


def BFS(start, goal, cycle_detect=False, verbose=False):
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
            print(len(path))    #print length of solution for convinience
            return path
        for next_vertex in neighbors(last_vertex):
            if cycle_detect:    #include cycle detection if asked for
                if next_vertex in path:
                    continue
            new_path = path + [next_vertex]
            frontier.append(new_path)
    return None


if __name__ == '__main__':
    start_time = time.time()

    # test_matrix, exit_row = read.read('encoding.txt')
    test_matrix, exit_row = [[2,1,1,0], [0,1,0,0], [1,1,0,0]], 2
    path  = BFS(test_matrix, exit_row, False, True)

    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence
