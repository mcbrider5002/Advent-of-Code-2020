import itertools
from math import prod

with open("input.txt", 'r') as f:
    numbers = [int(ln.strip()) for ln in f if ln.strip() != ""]
    
def find_sum(target, n, numbers):
    for nums in itertools.combinations(numbers, n):
        if(sum(nums) == target): return "{} == {}, {} == {}".format(" + ".join(str(num) for num in nums), target, " * ".join(str(num) for num in nums), prod(nums))
    return "Not found!"
    
print(f"Pt1: {find_sum(2020, 2, numbers)}\nPt2: {find_sum(2020, 3, numbers)}")