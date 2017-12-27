#!/usr/bin/env python
import math
import itertools

f = open('input', 'r')
data = f.readline().strip()
f.close()

value = int(data)

#value = 1024

def gen_tier(tier):
    # tier is zero based
    # order: bottom, left, top, right
    if tier == 0:
        return [range(1,2)] * 4

    max_sqrt = int((tier * 2) + 1)
    max = max_sqrt ** 2

    return (range(max-(max_sqrt-1), max+1),
            range(max-2*(max_sqrt-1), max-(max_sqrt-1)+1),
            range(max-3*(max_sqrt-1), max-2*(max_sqrt-1)+1))


# find the max value (lower right hand corner) must be odd
max_rt = int(math.ceil(math.sqrt(value)))
if max_rt % 2 == 0:
    max_rt += 1
max = max_rt ** 2
tier_n = (max_rt - 1) / 2
tier = gen_tier(tier_n)

for side in tier:
    if value in side:
        dist_from_middle = abs(value - side[int(len(side)/2)])
        break

print dist_from_middle
print dist_from_middle + tier_n


def spiral_walk():
    pos = (0,0)
    yield pos
    
    steps_taken = 1
    tier = 1
    while True:
        x = tier * 2
        for move in [(1,0)] + [(0,1)]*(x-1) + [(-1,0)]*x + [(0,-1)]*x + [(1,0)]*x:
            pos = tuple([sum(els) for els in zip(pos, move)])
            yield pos
            steps_taken += 1

        tier += 1

def sum_neighbors(arr, x, y):
    sum_val = 0
    # includes (0,0) which is ok for this problem
    for move in itertools.product([-1,0,1],[-1,0,1]):
        getx, gety = tuple([sum(els) for els in zip((x,y), move)])
        sum_val += arr[getx][gety]
    return sum_val


gen = spiral_walk()
val = 0
while val != value:
    pos = gen.next()
    val += 1

dist = sum(map(abs, pos))
print 'Part 1: manhatten dist %d' % dist

grid = [[0 for x in xrange(max_rt)] for y in xrange(max_rt)]
offset = int((max_rt - 1) / 2)

# treat the first square specially
gen = spiral_walk()
gen.next()
grid[offset][offset] = 1

for x,y in gen:
    sum_val = sum_neighbors(grid, x+offset, y+offset)
    grid[x+offset][y+offset] = sum_val

    if sum_val > value:
        break

print 'Part 2: first value greater %d at %d,%d' % (sum_val, x+offset, y+offset)


