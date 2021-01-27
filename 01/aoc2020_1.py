import itertools
from math import prod

with open("input.txt", 'r') as f:
    numbers = [int(ln.strip()) for ln in f if ln != ""]
    
def find_sum(target, n, numbers):
    for nums in itertools.combinations(numbers, n):
        if(sum(nums) == target): return "{} == {}, {} == {}".format(" + ".join(str(num) for num in nums), target, " * ".join(str(num) for num in nums), prod(nums))
    return "Not found!"
    
pt1, pt2 = find_sum(2020, 2, numbers), find_sum(2020, 3, numbers)
print("Pt1: {}\nPt2: {}".format(pt1, pt2))