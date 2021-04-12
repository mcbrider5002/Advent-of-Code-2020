with open("input.txt", 'r') as f:
    contents = f.readline().split(',')
def solve(turns):
    memory = {int(x) : i for i, x in enumerate(contents[:-1])}
    n = int(contents[-1])
    for i in range(len(contents) - 1, turns - 1):
        new_n = i - memory[n] if n in memory else 0
        memory[n] = i
        n = new_n
    return n
print(f"Pt1: {solve(2020)}\nPt2: {solve(30000000)}")