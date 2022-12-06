def part_a():
    with open("../../../../input/day4.txt") as f:
        content = f.read().split("\n")
    score = 0
    for line in content:
        if line == "":
            continue
        elf1, elf2 = line.split(",")
        elf1 = [int(i) for i in elf1.split("-")]
        elf2 = [int(i) for i in elf2.split("-")]

        if rinr(elf1, elf2) or rinr(elf2, elf1):
            score += 1
    print("Part a")
    print(score)


def rinr(r1, r2):
    return r1[0] <= r2[0] and r1[1] >= r2[1]

def part_b():
    with open("../../../../input/day4.txt") as f:
        content = f.read().split("\n")
    score = 0
    for line in content:
        if line == "":
            continue
        elf1, elf2 = line.split(",")
        elf1 = [int(i) for i in elf1.split("-")]
        elf2 = [int(i) for i in elf2.split("-")]

        if rinrb(elf1, elf2) or rinrb(elf2, elf1):
            print(line)
            score += 1
    print("Part b")
    print(score)

def rinrb(r1, r2):
    return r1[0] in range(r2[0], r2[1]+1) or r1[1] in range(r2[0], r2[1]+1)


part_a()
part_b()