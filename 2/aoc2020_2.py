from collections import Counter

with open("input.txt", 'r') as f:
    def parse_line(ln):
        def inner_strip(ls): return (x.strip() for x in ls)
        pre, pword = inner_strip(ln.strip().split(":"))
        pre, chr = inner_strip(pre.strip().split(" "))
        lower, upper = inner_strip(pre.strip().split("-"))
        return int(lower), int(upper), chr, pword
    
    inputs = [parse_line(ln) for ln in f if ln != ""]
    
def pt1(): return sum(Counter(pword).get(chr, 0) in range(lower, upper + 1) for lower, upper, chr, pword in inputs)
def pt2(): return sum((pword[lower - 1] == chr) ^ (pword[upper - 1] == chr) for lower, upper, chr, pword in inputs)
    
print("Pt1: {}\nPt2: {}".format(pt1(), pt2()))