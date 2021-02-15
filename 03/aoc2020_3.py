from math import prod
with open("input.txt", 'r') as f: 
    grid = [[ch == '#' for ch in ln.strip()] for ln in f if ln.strip() != ""]
def ski(xshift, yshift): return sum(grid[i * yshift][i * xshift % len(grid[0])] for i in range(len(grid) // yshift))
print(f"Pt1: {ski(3, 1)}\nPt2: {prod(ski(x, y) for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])}")