import re

stacks = [
    ["J", "H", "G", "M", "Z", "N", "T", "F"],
    ["V", "W", "J"],
    ["G", "V", "L", "J", "B", "T", "H"],
    ["B", "P", "J", "N", "C", "D", "V", "L"],
    ["F", "W", "S", "M", "P", "R", "G"],
    ["G", "H", "C", "F", "B", "N", "V", "M"],
    ["D", "H", "G", "M", "R"],
    ["H", "N", "M", "V", "Z", "D"],
    ["G", "N", "F", "H"]
    ]

#stacks = [
#    ["Z", "N"],
#    ["M", "C", "D"],
#    ["P"]
#    ]

def part_a():
    with open("../../../../input/day5.txt") as f:
        initial_setup, actions = f.read().split("\n\n")
    
    print(actions[-1])
    for line in actions.split("\n")[:-1]:
        numbers = [int(x) for x in re.findall(r'\d+', line)]
        for i in range(numbers[0]):
            to_move = stacks[numbers[1]-1].pop()
            stacks[numbers[2]-1].append(to_move)

    print(stacks)
    for s in stacks:
        print(s[-1], end="")

def part_b():
    with open("../../../../input/day5.txt") as f:
        initial_setup, actions = f.read().split("\n\n")
    
    for line in actions.split("\n")[:-1]:
        numbers = [int(x) for x in re.findall(r'\d+', line)]
        to_move = stacks[numbers[1]-1][-numbers[0]:]
        stacks[numbers[1]-1] = stacks[numbers[1]-1][:-numbers[0]]
        [stacks[numbers[2]-1].append(x) for x in to_move]

    for s in stacks:
        print(s[-1], end="")
    
        
part_b()
