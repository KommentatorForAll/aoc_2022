import re
import time

t0 = time.time()
def part_b():
    mv = 4000000
    start_x = mv // 2

    with open("input.txt") as f:
        content = f.read()[:-1].split("\n")

    scanner = []
    for line in content:
        sx, sy, bx, by = [int(x) for x in re.findall(r"\d+", line)]
        d = abs(sx-bx) + abs(sy-by)
        scanner.append((sx, sy, d))

    global hops
    for y in range(770000, mv):
        hiy = []
        # if y % 10000 == 0:
        #    print(f"{y=}, {hops=}")
        #    hops = 0
        x = start_x
        while x < mv:
            x, hiy = get_new_pos(x, y, scanner, hiy)
        #     hops += 1


hops = 0


def get_new_pos(x, y, scanner, hiy):
    i = 0
    for sx, sy, sd in scanner:
        dx = abs(x-sx)
        dy = abs(y-sy)
        d = dx + dy

        if d <= sd:
            if i in hiy:
                print("somethings definitely wrong....")
                print(hiy)
                print(f"{sx=}, {sy=}, {sd=}, {x=}, {y=}, {dx=}, {dy=}, {sx+(sd-dy)=}")
            hiy.append(i)
            return sx+(sd-dy)+1, hiy
        i += 1
    print(f"found at {x=}, {y=}, of score {x*4000000+y}")
    global t0
    print(f"done after {time.time()-t0}s")
    exit(0)


if __name__ == '__main__':
    part_b()
