from math import prod

with open("input.txt", 'r') as f:  
    grid = [[chr == '#' for chr in ln.strip()] for ln in f if ln != ""]
    
def ski(xshift, yshift): return sum(grid[i * yshift][i * xshift % len(grid[0])] for i in range(0, len(grid) // yshift))
    
pt1, pt2 = ski(3, 1), prod(ski(*args) for args in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])
print("Pt1: {}\nPt2: {}".format(pt1, pt2))