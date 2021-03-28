import re

mem_re = re.compile("mem\[([0-9]+)\]")
memory, memory2, or_mask, and_mask, mem_masks = {}, {}, 0, 2 ** 36, [(0, 2 ** 36)]
with open("input.txt", "r") as f:
    for ln in f:
        op, value = ln.split('=')
        if(op.strip() == "mask"):
            or_mask, and_mask, mem_masks = 0, 0, [(0, 0)]
            for i, ch in enumerate(reversed(value.strip())):
                or_mask += (ch != "X" and int(ch)) * (2 ** i)
                and_mask += (ch == "X" or int(ch)) * (2 ** i)
                if(ch == "X"): mem_masks.extend([(o + 2 ** i, a + 2 ** i) for o, a in mem_masks])
                elif(ch == "1"): mem_masks = [(o + 2 ** i, a + 2 ** i) for o, a in mem_masks]
                elif(ch == "0"): mem_masks = [(o, a + 2 ** i) for o, a in mem_masks]
        else:
            loc = int(mem_re.search(ln).group(1))
            memory[loc] = (int(value.strip()) | or_mask) & and_mask
            for o, a in mem_masks: memory2[(loc | o) & a] = int(value.strip())

print(f"Pt1: {sum(v for _, v in memory.items())}\nPt2: {sum(v for _, v in memory2.items())}")