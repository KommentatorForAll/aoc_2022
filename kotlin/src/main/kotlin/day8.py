import numpy as np


def part_a():
    with open("input.txt") as f:
        content = f.read().split("\n")
        content = [[int(i) for i in x] for x in content]
    trees = np.array(content)
    forest_shape = trees.shape
    viewable_trees = 0
    for i in range(1, forest_shape[0]-1):
        for j in range(1, forest_shape[1]-1):
            slices = [
                trees[0:i, j],
                trees[i+1:, j],
                trees[i, 0:j],
                trees[i, j+1:]
            ]
            height = trees[i, j]
            # print(f"{i=}, {j=}, {height=}")
            slices = [slc < height for slc in slices]
            if any([all(slc) for slc in slices]):
                viewable_trees += 1
                # print("visible")
    print(viewable_trees + ((trees.shape[0]-1)*4))


def part_b():
    with open("input.txt") as f:
        content = f.read().split("\n")
        content = [[int(i) for i in x] for x in content]
    trees = np.array(content)
    forest_shape = trees.shape
    highest_score = 0
    for i in range(1, forest_shape[0]-1):
        for j in range(1, forest_shape[1]-1):
            score = get_score(trees, i, j)
            highest_score = max(score, highest_score)
    print(highest_score)


def get_score(trees, i, j):
    x = i-1
    y = j
    height = trees[i, j]
    score = 0
    total_score = 1
    while x >= 0:
        score += 1
        if trees[x, y] >= height:
            break
        x -= 1
    end = trees.shape[0]
    total_score *= score
    score = 0

    x = i+1
    y = j
    while x < end:
        score += 1
        if trees[x, y] >= height:
            break
        x += 1

    x = i
    y = j -1
    total_score *= score
    score = 0
    while y >= 0:
        score += 1
        if trees[x, y] >= height:
            break
        y -= 1
    total_score *= score
    score = 0
    x = i
    y = j+1
    while y < end:
        score += 1
        if trees[x, y] >= height:
            break
        y += 1

    total_score *= score
    return total_score


if __name__ == '__main__':
    part_b()
