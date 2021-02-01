import copy

with open("input.txt", "r") as f:
    data = [[chr for chr in ln.strip() if chr] for ln in f if ln.strip() != ""]

def adj_indices(grid, i, j):
    return ((k, l) for k in range(i-1, i+2) for l in range(j-1, j+2) if 0 <= k < len(grid) and 0 <= l < len(grid[0]) and (k != i or l != j))

def sight_indices(grid, i, j):
    idxes = []
    for k, l in ((k, l) for k in [-1, 0, 1] for l in [-1, 0, 1] if k != 0 or l != 0):
        m, i2, j2 = 1, (i + k), (j + l)
        while(0 <= i2 < len(grid) and 0 <= j2 < len(grid[0])):
            current = grid[i2][j2]
            if(current == '#' or current == 'L'):
                idxes.append((i2, j2))
                break
            m, i2, j2 = (m + 1), (i + k * m), (j + l * m)
    return idxes

def grid_shenanigans(idx_fn, threshold):
    mutated = True
    grid = copy.deepcopy(data)
    while(mutated):
        mutated = False
        adjs = [[0 for chr in ln] for ln in grid]
        for i, ln in enumerate(grid):
            for j, chr in enumerate(ln):
                if(chr == '#'): 
                    for (k, l) in idx_fn(grid, i, j): adjs[k][l] += 1
        for i, ln in enumerate(grid):
            for j, chr in enumerate(ln):
                if(chr == '#' and adjs[i][j] >= threshold): 
                    grid[i][j] = 'L'
                    mutated = True
                elif(chr == 'L' and adjs[i][j] == 0): 
                    grid[i][j] = '#'
                    mutated = True
    return sum(chr == '#' for ln in grid for chr in ln)
    
pt1, pt2 = grid_shenanigans(adj_indices, 4), grid_shenanigans(sight_indices, 5)
print("Pt1: {}\nPt2: {}".format(pt1, pt2))