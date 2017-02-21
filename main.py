import read, rank, unrank, BFS, DFS, mechanics, BFS, LCFS, DFS, DEEP
import time, numpy, copy

# start_time = time.time()    #start keeping track of time
# print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence

if __name__ == '__main__':

    #showcases for all functions below

    '''
    ### read ###
    parameters: encoded textfile
    return: matrix representation, goal row
    '''

    test_matrix, exit = read.read('encoding.txt') ###function call is here
    print("!!! read !!!")
    print("state matrix:\n", numpy.matrix(test_matrix))
    print("exit row:", exit, "\n")

    '''
    ### rank ###
    parameters: matrix representation
    return: corresponding integer
    '''
    print("!!! rank !!!")
    integer = rank.rank(test_matrix)
    print("integer:", integer)


    '''
    ### unrank ###
    parameters: integer, bases array, array of block patterns, num of columns
    return: corresponding matrix
    '''
    print("\n!!! unrank !!!")
    integer = 174
    bases = [2, 3, 4, 11]
    block_pattern = [[1,1,0,0,1,1], [1,0,1,0,1], [1,1,0,1]]
    num_columns = 7
    test_matrix = unrank.unrank(integer, bases, block_pattern, num_columns)
    print("corresponding matrix:\n",numpy.matrix(test_matrix),"\n")


    '''
    ### BFS w/o rank/unrank ###
    parameters: start matrix, goal row, cycle_detection, verbose
    return: path to goal (or none if no such path)
    '''
    print("\n!!! BFS w/o rank/unrank !!!")
    start_time = time.time()    #start keeping track of time
    BFS.BFS(test_matrix, exit, cycle_detection=True, verbose=False)
    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence


    '''
    ### BFS w rank/unrank ###
    parameters: start matrix, goal row, cycle_detection, verbose
    return: path to goal (or none if no such path)
    '''
    print("\n!!! BFS with rank/unrank !!!")
    start_time = time.time()    #start keeping track of time
    BFS.BFS2(test_matrix, exit, cycle_detection=True, verbose=False)
    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence


    '''
    ### LCFS w rank/unrank ###
    parameters: start matrix, goal row, cycle_detection, verbose
    return: path to goal (or none if no such path)
    '''
    print("\n!!! LCFS w/o rank/unrank !!!")
    start_time = time.time()    #start keeping track of time
    LCFS.LCFS(test_matrix, exit, cycle_detection=True, verbose=False)
    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence


    '''
    ### LCFS with rank/unrank and pruning ###
    parameters: start matrix, goal row, pruning, verbose
    return: path to goal (or none if no such path)
    '''
    print("\n!!! LCFS with rank/unrank and pruning !!!")
    start_time = time.time()    #start keeping track of time
    LCFS.LCFS2(test_matrix, exit, True, verbose=False)
    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence


    '''
    ### DFS w/o rank/unrank ###
    ### DFS with rank/unrank ###
    parameters: start matrix, goal row, verbose
    return: path to goal (or none if no such path)
    NOTE: uncommented because it enters loop and never finishes
    '''
    print("\n!!! DFS w/o rank/unrank !!!")
    print("\n!!! DFS with rank/unrank !!!")
    # DFS.DFS(test_matrix, exit, verbose=False)


    '''
    ### DFS_cycle w/o rank/unrank ###
    parameters: start matrix, goal row, verbose
    return: path to goal (or none if no such path)
    '''
    print("\n!!! DFS_cycle w/o rank/unrank !!!")
    start_time = time.time()    #start keeping track of time
    DFS.DFS_cycle(test_matrix, exit, verbose=False)
    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence

    '''
    ### DFS_cycle with rank/unrank ###
    parameters: start matrix, goal row, verbose
    return: path to goal (or none if no such path)
    '''
    print("\n!!! DFS_cycle with rank/unrank !!!")
    start_time = time.time()    #start keeping track of time
    DFS.DFS_cycle2(test_matrix, exit, verbose=False)
    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence

    '''
    ### DFS_prune w/o rank/unrank ###
    parameters: start matrix, goal row, verbose
    return: path to goal (or none if no such path)
    NOTE: testing on smaller matrix than for other graph, because too slow
    '''
    print("\n!!! DFS_prune w/o rank/unrank! !!!")
    start_time = time.time()    #start keeping track of time
    test_matrix2, exit2 = [[2,1,1,0], [0,1,0,0], [1,1,0,0]], 2
    DFS.DFS_prune(test_matrix2, exit2, verbose=False)
    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence


    '''
    ### DFS_prune with rank/unrank ###
    parameters: start matrix, goal row, verbose
    return: path to goal (or none if no such path)
    '''
    print("\n!!! DFS_prune with rank/unrank! !!!")
    start_time = time.time()    #start keeping track of time
    DFS.DFS_prune2(test_matrix, exit, verbose=False)
    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence


    '''
    ### DFS_bound w/o rank/unrank ###
    parameters: start matrix, goal row, depth, cycle_detection, verbose
    return: path to goal (or none if no such path)
    '''
    print("\n!!! DFS_bound w/o rank/unrank! !!!")
    start_time = time.time()    #start keeping track of time
    DFS.DFS_bound(test_matrix, exit, 36, cycle_detection=True, verbose=False)
    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence

    '''
    ### DFS_bound with rank/unrank ###
    parameters: start matrix, goal row, depth, cycle_detection, verbose
    return: path to goal (or none if no such path)
    '''
    print("\n!!! DFS_bound with rank/unrank! !!!")
    start_time = time.time()    #start keeping track of time
    DFS.DFS_bound(test_matrix, exit, 36, cycle_detection=True, verbose=False)
    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence

    '''
    ### DEEP w/o rank/unrank ###
    parameters: start matrix, goal row, cycle_detection, verbose
    return: path to goal (or none if no such path)
    '''
    print("\n!!! DEEP w/o rank/unrank! !!!")
    start_time = time.time()    #start keeping track of time
    DEEP.DEEP(test_matrix, exit, cycle_detection=True, verbose=False)
    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence

    '''
    ### DEEP with rank/unrank ###
    parameters: start matrix, goal row, cycle_detection, verbose
    return: path to goal (or none if no such path)
    '''
    print("\n!!! DEEP with rank/unrank! !!!")
    start_time = time.time()    #start keeping track of time
    DEEP.DEEP2(test_matrix, exit, cycle_detection=True, verbose=False)
    print("--- %s seconds ---" % (time.time() - start_time)) #print time for convinence

    print()
    print("END")
