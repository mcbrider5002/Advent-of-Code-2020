from collections import Counter

with open("input.txt", "r") as f:
    numbers = [0] + sorted(int(ln.strip()) for ln in f if ln.strip() != "")

def pt1():
    counts = Counter((y - x) for x, y in zip(numbers, numbers[1:]))
    return counts[1] * (counts[3] + 1)
    
def pt2():
    ns = set(numbers)
    prevs = 1, 0, 0
    for i in numbers[1:]:
        prev_counts = ((i-3) in ns) + ((i-2) in ns) + ((i-1) in ns)
        new = sum(prevs[:prev_counts])
        prevs = new, prevs[0], prevs[1]
    return prevs[0]

print(f"Pt1: {pt1()}\nPt2: {pt2()}")