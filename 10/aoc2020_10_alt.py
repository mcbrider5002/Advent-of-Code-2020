with open("input.txt", "r") as f:
    numbers = [int(ln.strip()) for ln in f if ln.strip() != ""]
max_n = max(numbers)
num_array = [True] + [False] * max_n
for n in numbers: num_array[n] = True  

def pt1():
    count_1, count_3 = (num_array[1]) + (num_array[1] and num_array[2]), 0
    for n in range(3, max_n + 1):
        if(num_array[n]):
            if(num_array[n - 1]): count_1 += 1
            elif(num_array[n - 2]): pass
            else: count_3 += 1
    return count_1 * (count_3 + 1)
    
def pt2():
    if(num_array[1] and num_array[2]): prevs = 2, 1, 1
    elif(num_array[1] or num_array[2]): prevs = 1, 1, 0
    else: prevs = 1, 0, 0
    for n in range(3, max_n + 1):
        if(num_array[n]):
            prev_counts = num_array[n-3] + num_array[n-2] + num_array[n-1]
            new = sum(prevs[:prev_counts])
            prevs = new, prevs[0], prevs[1]
    return prevs[0]

print(f"Pt1: {pt1()}\nPt2: {pt2()}")