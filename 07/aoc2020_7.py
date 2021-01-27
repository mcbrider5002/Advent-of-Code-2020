from collections import defaultdict
from functools import reduce

def to_entry(ln):
        bags = ln.replace("bags", "bag").split("bag")[:-1]
        outer = " ".join(bags[0].strip().split(" ")[-2:])
        if "no other" in ln: return (outer, [])
        inners = [(int(bs.strip().split(" ")[-3]), " ".join(bs.strip().split(" ")[-2:])) for bs in bags[1:]]
        return (outer, inners)

forwards, backwards = {}, defaultdict(set)        
with open("input.txt", 'r') as f:
    for outer, inners in (to_entry(ln) for ln in f if ln.strip()):
        forwards[outer] = inners
        print(outer, inners)
        for _, inn in inners: backwards[inn].add(outer)
        
def pt1(s): return s | reduce(lambda x, y: x | y, (pt1(backwards.get(k, set())) for k in s), set())
def pt2(ls): return sum(n * (pt2(forwards.get(x, [])) + 1) for n, x in ls) if ls else 0
    
print("pt1: {}\npt2: {}".format(len(pt1(backwards["shiny gold"])), pt2(forwards["shiny gold"])))