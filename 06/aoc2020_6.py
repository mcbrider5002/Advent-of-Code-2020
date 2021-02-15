from functools import reduce
with open("input.txt", 'r') as f:
    groups = [[set(ln) for ln in group.split("\n") if ln.strip()] for group in f.read().split("\n\n")]
def sum_answers(fn): return sum(len(reduce(fn, group)) for group in groups)
print(f"Pt1: {sum_answers(lambda x, y: x | y)}\nPt2: {sum_answers(lambda x, y: x & y)}")