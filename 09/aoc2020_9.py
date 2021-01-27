from collections import deque

with open("input.txt", "r") as f:
    numbers = [int(l.strip()) for l in f if l.strip() != ""]

def pt1(prelength):
    sums = [set() for _ in numbers]
    for i, n in enumerate(numbers):
        for j in range(i, prelength): sums[i].add(n + numbers[j])
        
    for i in range(prelength, len(numbers)):
        if(not any(numbers[i] in sums[j] for j in range(i - prelength, i))): return numbers[i]
        for j in range(i - prelength + 1, i): sums[j].add(numbers[i] + numbers[j])
        
    return "Nothing found!"
    
def pt2(target):
    count, window = 0, deque([])
    for n in numbers:
        window.append(n)
        count += n
        while(count > target and len(window) > 0): count -= window.popleft()
        if(count == target): return min(window) + max(window)
    return "Nothing found!"

ans1 = pt1(25)
print("Pt1: {}\nPt2: {}".format(ans1, pt2(ans1)))