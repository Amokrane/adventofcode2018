import sys
import re
import numpy as np 

def calculate_largest_area(input_file):
    lines = [line.rstrip('\n') for line in open(input_file)]

    w, h = 400, 400 
    grid = [[-1 for x in xrange(w)] for y in xrange(h)]
    indexed_coords = {}
    indexed_coords_reverse = {}
    area_per_coords = {}

    idx = 0
    for line in lines:
        coords = re.split(", ", line)
        coord_x = int(coords[0])
        coord_y = int(coords[1])
        indexed_coords[line] = idx 
        indexed_coords_reverse[idx] = line
        grid[coord_y][coord_x] = idx
        idx += 1

    # at this point, we have a grid with the initial coords

    for i in range(h):
        for j in range(w):
            if(grid[i][j] >= 0):
                continue;

            distance_memo = {}
            is_tie = False
            shortest_distance = 1000

            for line in lines:
                coords = re.split(", ", line)
                d = calculate_manhattan_distance(coords, [j, i])
                distance_memo[d] = distance_memo.get(d, 0) + 1

                if(d <= shortest_distance):
                    if(distance_memo[d] > 1):
                        is_tie = True
                    else:
                        is_tie = False

                    closest_coords = line 
                    shortest_distance = d

            if(not is_tie):
                closest_coord_index = indexed_coords[closest_coords]
                grid[i][j] = closest_coord_index
                area_per_coords[closest_coord_index] = area_per_coords.get(closest_coord_index, 0) + 1
            else:
                grid[i][j] = -2

    print_grid(grid)

    not_infinite_values = []
    for key, value in area_per_coords.iteritems():
        line = indexed_coords_reverse[key]
        coords = re.split(", ", line) 
        c_x = int(coords[0])
        c_y = int(coords[1])
        infinite = False

        a = False
        b = False
        c = False
        d = False

        while(c_x >= 0):
            if(grid[c_y][c_x] != indexed_coords[line] and grid[c_y][c_x] != -1):
                a =  True
                break
            c_x -= 1

        c_x = int(coords[0])
        c_y = int(coords[1])
        while(c_x < w):
            if(grid[c_y][c_x] != indexed_coords[line] and grid[c_y][c_x] != -1):
                b = True
                break
            c_x += 1

        c_x = int(coords[0])
        c_y = int(coords[1])
        while(c_y >= 0):
            if(grid[c_y][c_x] != indexed_coords[line] and grid[c_y][c_x] != -1):
                c = True
                break
            c_y -= 1

        c_x = int(coords[0])
        c_y = int(coords[1])
        while(c_y < h):
            if(grid[c_y][c_x] != indexed_coords[line] and grid[c_y][c_x] != -1):
                d = True
                break
            c_y += 1

        if ((not a) or (not b) or (not c) or (not d)):
            infinite = True

        if(not infinite):
            not_infinite_values.append(value)

    print(max(not_infinite_values) + 1)
    
    # part 2

    count = 0
    for i in range(h):
        for j in range(w):
            sum = 0

            for coords_str in lines:
                coords = re.split(", ", coords_str)
                sum += calculate_manhattan_distance(coords, [j, i])
            
            if(sum < 10000):
                count += 1
    print(count)
                

def calculate_manhattan_distance(coord_a, coord_b):
    return abs(int(coord_a[0]) - int(coord_b[0])) + abs(int(coord_a[1]) - int(coord_b[1])) 

def print_grid(grid):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in grid]))

if  __name__ == "__main__":
    calculate_largest_area(sys.argv[1])

