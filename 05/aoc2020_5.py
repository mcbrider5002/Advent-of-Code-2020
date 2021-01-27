with open("input.txt", "r") as f:
    lines = [l.strip() for l in f if l.strip() != ""]

def seat_id(specifier):
    pre, post = specifier[:7], specifier[7:]
    def get_posn(sp): return sum(2 ** i if d else 0 for i, d in enumerate(reversed(sp)))
    row_no = get_posn([ch == "B" for ch in pre])
    col_no = get_posn([ch == "R" for ch in post])
    id = row_no * 8 + col_no
    return row_no, col_no, id

def find_seat(specifiers):
    ls = [True] * (128 * 8)
    for specifier in specifiers:
        _, _, id = seat_id(specifier)
        ls[id] = False
    return ls.index(True, ls.index(False) + 1)

pt1, pt2 = max(seat_id(ln)[2] for ln in lines), find_seat(lines)
print("Pt1: {}\nPt2: {}".format(pt1, pt2))