from collections import defaultdict
from functools import reduce
import re

def to_entry(ln):
    outer_bag = ln[:ln.find("bags")].strip()
    matches = re.compile(r"([0-9]+) ([a-zA-Z ]+) (bag|bags)").findall(ln)
    inner_bags = [(int(n), bag) for n, bag, _ in matches]
    return outer_bag, inner_bags

forwards, backwards = dict(), defaultdict(set)        
with open("input.txt", 'r') as f:
    for outer, inners in (to_entry(ln) for ln in f if ln.strip()):
        forwards[outer] = inners
        for _, inn in inners: backwards[inn].add(outer)
        
def pt1(s): return reduce(lambda x, y: x | y, (pt1(backwards[k]) for k in s), s)
def pt2(ls): return sum(n * (pt2(forwards[x]) + 1) for n, x in ls) if ls else 0
    
print("Pt1: {}\nPt2: {}".format(len(pt1(backwards["shiny gold"])), pt2(forwards["shiny gold"])))