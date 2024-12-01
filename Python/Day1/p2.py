from collections import Counter
with open("input.txt", "r") as f:
    puzz_inp = f.read()
first_l = []
second_l = []
for line in puzz_inp.split("\n"):
    line = line.split()
    if line:
        first_l.append(line[0].strip())
        second_l.append(line[1].strip())
first_l = [int(num) for num in first_l]
second_l = [int(num) for num in second_l]
def solution(l1: list[int], l2: list[int]):
    counter = Counter(l2)
    sim_score = 0
    
    for num in l1:
        freq = counter[num]
        sim_score += (freq * num)
    return sim_score
print(solution(first_l, second_l))