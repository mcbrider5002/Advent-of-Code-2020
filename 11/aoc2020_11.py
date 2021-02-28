import itertools

with open("input.txt", "r") as f:
    data = [[ch for ch in ln.strip() if ch] for ln in f if ln.strip() != ""]
rows = [(i, 0) for i in range(len(data))]
columns = [(0, j) for j in range(len(data[0]))]

class Seat():
    def __init__(self, occupied):
        self.occupied = occupied
        self.adjacent = 0
        self.adjacents = set()
        self.perm_occupied = 0
        
    def lock(self, i, j, updates, grid, threshold):
        if(self.occupied and (len(self.adjacents) + self.perm_occupied < threshold) or not self.occupied and self.perm_occupied > 0):
            for i2, j2 in self.adjacents:
                current = grid[i2][j2]
                if(self.occupied): current.perm_occupied += 1
                current.adjacents.remove((i, j))
            return True
        return False

def all_straights():
    def to_range(istart, jstart, istep, jstep):
        return zip(
            range(istart, len(data), istep) if istep != 0 else itertools.repeat(istart), 
            range(jstart, -1 if jstep < 0 else len(data[0]), jstep) if jstep != 0 else itertools.repeat(jstart)
        )

    steps = itertools.chain(
        ((pt, 0, 1) for pt in rows),
        ((pt, 1, 0) for pt in columns),
        ((pt, 1, 1) for pt in itertools.chain(rows, columns)),
        ((pt, 1, -1) for pt in itertools.chain(((i, len(data[0]) - 1) for i, _ in rows), columns))
    )
    
    return (to_range(istart, jstart, istep, jstep) for (istart, jstart), istep, jstep in steps)

def adj_indices(grid):
    for pts in all_straights():
        line = [(i, j, grid[i][j]) for i, j in pts]
        for k in range(len(line) - 1):
            i, j, x = line[k]
            i2, j2, x2 = line[k+1]
            if(not x is None and not x2 is None):
                x.adjacents.add((i2, j2))
                x2.adjacents.add((i, j))
    
def sight_indices(grid):
    for pts in all_straights():
        prev = None
        for i, j in pts:
            if(not grid[i][j] is None):
                if(not prev is None):
                    i2, j2 = prev
                    grid[i][j].adjacents.add((i2, j2))
                    grid[i2][j2].adjacents.add((i, j))
                prev = i, j
    
def grid_shenanigans(populate_adjacent, threshold):
    mutated = True
    grid = [[Seat(False) if s == "L" else (Seat(True) if s == "#" else None) for s in row] for row in data]
    updates = {(i, j) for i, row in enumerate(data) for j, _ in enumerate(row) if not grid[i][j] is None}
    populate_adjacent(grid)
    while(mutated):
        mutated = False
        for i, j in updates:
            current = grid[i][j]
            current.adjacent = current.perm_occupied + sum(grid[i2][j2].occupied for i2, j2 in current.adjacents)
        for i, j in updates:
            current = grid[i][j]
            if(current.occupied and current.adjacent >= threshold or not current.occupied and current.adjacent == 0):
                current.occupied = not current.occupied
                mutated = True
        locked = set()
        for i, j in updates:
            if(grid[i][j].lock(i, j, updates, grid, threshold)): locked.add((i, j))
        updates -= locked
    return sum(not x is None and x.occupied for row in grid for x in row)
    
print(f"Pt1: {grid_shenanigans(adj_indices, 4)}\nPt2: {grid_shenanigans(sight_indices, 5)}")