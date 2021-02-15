with open("input.txt", "r") as f:
    lines = [ln.strip() for ln in f if ln.strip() != ""]

def seat_id(specifier):
    pre, post = specifier[:7], specifier[7:]
    def get_posn(sp): return sum(2 ** i if d else 0 for i, d in enumerate(reversed(sp)))
    row_no = get_posn([ch == "B" for ch in pre])
    col_no = get_posn([ch == "R" for ch in post])
    return row_no * 8 + col_no

def find_seat(specifiers):
    ls = [True] * (128 * 8)
    for specifier in specifiers: ls[seat_id(specifier)] = False
    return ls.index(True, ls.index(False) + 1)

print(f"Pt1: {max(seat_id(ln) for ln in lines)}\nPt2: {find_seat(lines)}")