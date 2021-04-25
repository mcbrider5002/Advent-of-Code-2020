from math import prod
import re

with open("input.txt", 'r') as f:
    fields, yours, others = f.read().split("\n\n")
    fields = re.compile(r"([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)").findall(fields)
    fields = [(name, range(int(r1_start), int(r1_end) + 1), range(int(r2_start), int(r2_end) + 1)) for name, r1_start, r1_end, r2_start, r2_end in fields]
    yours = [int(x) for x in yours.split("\n")[1].split(',')]
    others = [[int(x) for x in o.split(',')] for o in others.split("\n")[1:] if o.strip() != ""]
    
all_ranges = [r for t in fields for r in t[1:]]
valid_tickets = [o for o in others if all(any(x in r for r in all_ranges) for x in o)]
allocated, allocations = 0, [""] * len(valid_tickets[0])
field_domains = [[dom[0] for dom in fields if all(any(valid_tickets[i][j] in r for r in dom[1:]) for i in range(len(valid_tickets)))] for j in range(len(valid_tickets[0]))]
while(allocated < len(allocations)):
    unit_idx, unit_dom = next((i, d[0]) for i, d in enumerate(field_domains) if len(d) == 1)
    allocations[unit_idx] = unit_dom
    allocated += 1
    for d in field_domains:
        if(unit_dom in d): d.remove(unit_dom)
        
pt1 = sum(x for o in others for x in o if all(not x in r for r in all_ranges))
pt2 = prod(yours[i] for i, name in enumerate(allocations) if name.startswith("departure"))
print(f"Pt1: {pt1}\nPt2: {pt2}")