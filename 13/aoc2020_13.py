from itertools import count

with open("input.txt", "r") as f:
    target = int(f.readline().strip())
    buses = sorted(((i, int(n.strip())) for i, n in enumerate(f.readline().split(',')) if n.strip().isnumeric()), key=lambda t: t[1], reverse=True)
    
first = min(((n, n * (target // n + 1) - target) for _, n in buses), key=lambda t: t[1])

rems = [(n - (i) % n) % n for i, n in buses]
step, soln = 1, rems[0] 
for i in range(1, len(buses)):
    step = step * buses[i-1][1]
    soln = next(t for t in count(soln, step) if t % buses[i][1] == rems[i])

print(f"Pt1: {first[0] * first[1]}\nPt2: {soln}")