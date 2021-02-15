from collections import Counter
import re

with open("input.txt", 'r') as f:
    def parse_line(ln):
        m = re.compile(r"([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)").match(ln)
        return int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
    inputs = [parse_line(ln.strip()) for ln in f if ln.strip() != ""]
    
def pt1(): return sum(Counter(pword).get(ch, 0) in range(lower, upper + 1) for lower, upper, ch, pword in inputs)
def pt2(): return sum((pword[lower - 1] == ch) ^ (pword[upper - 1] == ch) for lower, upper, ch, pword in inputs)

print(f"Pt1: {pt1()}\nPt2: {pt2()}")