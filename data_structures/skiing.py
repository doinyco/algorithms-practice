# Imagine you have a 2D array that represents a ski slope. An index with a value of 1 represents a tree.
# The skier can only travel right and down along the array. 
# Write an algorithm to determine whether a clear path exists for the skier to cross the finish line.

def find_path(ski_slope):
    print(path_exist(ski_slope, 0, 0))

def path_exist(ski_slope, x, y):
    if x == len(ski_slope) or y == len(ski_slope[x]) or ski_slope[x][y] == 1:
        return False

    if x == len(ski_slope[-1]) and y == len(ski_slope[-1]): 
        return False

    return (path_exist(ski_slope, x+1, y) or path_exist(ski_slope,x, y+1))




ski_slope = [
    [0,1,1,0],
    [1,0,0,1],
    [0,1,0,1],
    [1,1,0,0]
]
find_path(ski_slope)

