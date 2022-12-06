def part_a():
    with open("../../../../input/day6.txt") as file:
        content = file.read()
    for i in range(len(content)-4):
        if len(set(content[i:i+4]))==4:
            print(i+4)
            return

def part_b():
    with open("../../../../input/day6.txt") as file:
        content = file.read()
    for i in range(len(content)-14):
        if len(set(content[i:i+14]))==14:
            print(i+14)
            return


part_b()
