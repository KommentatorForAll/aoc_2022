pta = True

class Monkey:
    def __init__(self, items, op, div, mt, mf):
        self.items = items
        self.op = op
        self.div = div
        self.mt = mt
        self.mf = mf
        self.operations = 0

    def throw_all(self, monkeys):
        for itm in self.items:
            v = self.op(itm) // 3 if pta else self.op(itm) % 9699690
            if v % self.div == 0:
                monkeys[self.mt].items.append(v)
            else:
                monkeys[self.mf].items.append(v)
            self.operations += 1
        self.items = []

    def __lt__(self, other):
        return self.operations < other.operations


def part_a():
    monkeys = [
        Monkey([53, 89, 62, 57, 74, 51, 83, 97], lambda x: x*3, 13, 1, 5),
        Monkey([85, 94, 97, 92, 56], lambda x: x+2, 19, 5, 2),
        Monkey([86, 82, 82], lambda x: x+1, 11, 3, 4),
        Monkey([94, 68], lambda x: x+5, 17, 7, 6),
        Monkey([83, 62, 74, 58, 96, 68, 85], lambda x: x+4, 3, 3, 6),
        Monkey([50, 68, 95, 82], lambda x: x+8, 7, 2, 4),
        Monkey([75], lambda x: x*7, 5, 7, 0),
        Monkey([92, 52, 85, 89, 68, 82], lambda x: x*x, 2, 0, 1)
    ]

    for i in range(20):
        print(i)
        for monkey in monkeys:
            monkey.throw_all(monkeys)
    print()
    [print(x.operations) for x in monkeys]
    global pta
    pta = False

    monkeys = [
        Monkey([53, 89, 62, 57, 74, 51, 83, 97], lambda x: x*3, 13, 1, 5),
        Monkey([85, 94, 97, 92, 56], lambda x: x+2, 19, 5, 2),
        Monkey([86, 82, 82], lambda x: x+1, 11, 3, 4),
        Monkey([94, 68], lambda x: x+5, 17, 7, 6),
        Monkey([83, 62, 74, 58, 96, 68, 85], lambda x: x+4, 3, 3, 6),
        Monkey([50, 68, 95, 82], lambda x: x+8, 7, 2, 4),
        Monkey([75], lambda x: x*7, 5, 7, 0),
        Monkey([92, 52, 85, 89, 68, 82], lambda x: x*x, 2, 0, 1)
    ]

    for i in range(10000):
        print(i)
        for monkey in monkeys:
            monkey.throw_all(monkeys)
    print()
    op = [x.operations for x in monkeys]
    op.sort()
    print(op)
    print(op[-1]*op[-2])
    lcm = 1
    for m in monkeys:
        lcm *= m.div
    print(lcm)


if __name__ == '__main__':
    part_a()
