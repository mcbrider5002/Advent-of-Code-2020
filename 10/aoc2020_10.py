from collections import Counter

with open("input.txt", "r") as f:
    numbers = [int(l.strip()) for l in f if l.strip() != ""]

srted = [0] + sorted(numbers)

def pt1():
    counts = Counter((y - x) for x, y in zip(srted, srted[1:]))
    return counts[1] * (counts[3] + 1)
    
def pt2():
    maxm = max(numbers)
    ns = set(numbers) | {0}
    prevs = 1, 0, 0
    for i in (i for i in range(srted[1], maxm+1) if i in ns):
        prev_counts = ((i-3) in ns) + ((i-2) in ns) + ((i-1) in ns)
        new = sum(prevs[:prev_counts])
        prevs = new, prevs[0], prevs[1]
    return prevs[0]

print("Pt1: {}\nPt2: {}".format(pt1(), pt2()))