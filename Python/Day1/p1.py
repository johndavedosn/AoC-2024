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
distances = []
def solution(l1: list[int], l2: list[int]):
    while l1 and l2:
        m_l1 = min(l1)
        m_l2 = min(l2)
        dist = m_l1 - m_l2
        distances.append(abs(dist))
        l1.remove(m_l1)
        l2.remove(m_l2)

solution(first_l, second_l)
print(sum(distances))