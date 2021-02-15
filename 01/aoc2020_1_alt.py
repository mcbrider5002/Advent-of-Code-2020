import itertools
from math import prod
from bisect import bisect_left

with open("input.txt", 'r') as f:
    numbers = sorted(int(ln.strip()) for ln in f if ln.strip() != "")
    
def find_sum(target, n, numbers):
    '''Like the other solution, but sorts the list and uses a binary search instead of one of the nested linear searches...'''
    for nums in itertools.combinations(enumerate(numbers), n - 1):
        start, to_find = max(i for i, _ in nums) + 1, target - sum(num for _, num in nums)
        i = bisect_left(numbers, to_find, lo=start)
        if i != len(numbers) and numbers[i] == to_find:
            new_nums = [n for _, n in nums] + [to_find]
            return "{} == {}, {} == {}".format(" + ".join(str(num) for num in new_nums), target, " * ".join(str(num) for num in new_nums), prod(new_nums))
    return "Not found!"
    
print(f"Pt1: {find_sum(2020, 2, numbers)}\nPt2: {find_sum(2020, 3, numbers)}")