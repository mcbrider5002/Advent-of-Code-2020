def seat_id(specifier):
    pre, post = specifier[:7], specifier[7:]
    def get_posn(sp): return sum(2 ** i if d else 0 for i, d in enumerate(reversed(sp)))
    row_no = get_posn([ch == "B" for ch in pre])
    col_no = get_posn([ch == "R" for ch in post])
    return row_no * 8 + col_no

with open("input.txt", "r") as f:
    numbers = set(seat_id(ln.strip()) for ln in f if ln.strip() != "")
minm, maxm = min(numbers), max(numbers)
print(f"Pt1: {maxm}\nPt2: {next(i for i in range(minm+1, maxm) if not i in numbers)}")