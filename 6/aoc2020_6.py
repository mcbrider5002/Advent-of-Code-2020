from functools import reduce
def set_reduce(answers, fn): return reduce(fn, (set(ln) for ln in answers.split("\n") if ln.strip()))
def sum_answers(fn):
    with open("input.txt", 'r') as f: return sum(len(set_reduce(group, fn)) for group in f.read().split("\n\n"))
print("pt 1: {}\npt 2: {}".format(sum_answers(lambda x, y: x | y), sum_answers(lambda x, y: x & y)))