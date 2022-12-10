import math

def part_a():
    positions = {(0, 0)}
    head = (0, 0)
    tail = (0, 0)

    with open("input.txt") as f:
        content = f.read().split("\n")

    for line in content:
        dir, cnt = line.split(" ")
        cnt = int(cnt)
        for i in range(cnt):
            match dir:
                case "R":
                    head = (head[0], head[1]+1)
                case "L":
                    head = (head[0], head[1]-1)
                case "U":
                    head = (head[0]-1, head[1])
                case "D":
                    head = (head[0]+1, head[1])
            tail = move_tail(head, tail)
            positions.add(tail)
            #print(head)
            #print(tail)
            #print()
        #print(positions)
        #print("\n")
    #print(positions)
    #print("\n\n")
    print(len(positions))


def sign(x):
    return 0 if x == 0 else math.copysign(1, x)

def move_tail(head, tail):
    distances = (head[0]-tail[0], head[1] - tail[1])
    sgn_distances = (sign(head[0]-tail[0]), sign(head[1] - tail[1]))
    if (distances[0] != 0 and abs(distances[1]) > 1) or (distances[1] != 0 and abs(distances[0]) > 1):
        return tail[0]+sgn_distances[0], tail[1] + sgn_distances[1]
    if abs(distances[0]) > 1:
        return tail[0]+sgn_distances[0], tail[1]
    if abs(distances[1]) > 1:
        return tail[0], tail[1] + sgn_distances[1]
    return tail

def part_b():
    positions = {(0, 0)}
    head = (0, 0)
    tails = [(0, 0) for _ in range(9)]

    with open("input.txt") as f:
        content = f.read().split("\n")

    for line in content:
        dir, cnt = line.split(" ")
        cnt = int(cnt)
        for _ in range(cnt):
            match dir:
                case "R":
                    head = (head[0], head[1]+1)
                case "L":
                    head = (head[0], head[1]-1)
                case "U":
                    head = (head[0]-1, head[1])
                case "D":
                    head = (head[0]+1, head[1])
            last_t = head
            for i, t in enumerate(tails):
                tails[i] = move_tail(last_t, t)
                last_t = tails[i]
            positions.add(tails[-1])
            print(head)
            print(tails)
            print()
        #print(positions)
        #print("\n")
    #print(positions)
    #print("\n\n")
    print(len(positions))

part_b()