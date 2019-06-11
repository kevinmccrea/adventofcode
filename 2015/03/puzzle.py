#!/usr/bin/env python

f = open('input.txt', 'r')
data = f.readline().strip()
f.close()

ops = dict()
ops['^'] = lambda loc: (loc[0], loc[1]+1)
ops['>'] = lambda loc: (loc[0]+1, loc[1])
ops['v'] = lambda loc: (loc[0], loc[1]-1)
ops['<'] = lambda loc: (loc[0]-1, loc[1])

current_loc = (0,0)
houses = dict()
houses[current_loc] = 1

santa_loc = (0,0)
robot_loc = (0,0)
toggle = True
houses_split = dict()
houses_split[santa_loc] = 1
for dir in data:
    current_loc = ops[dir](current_loc)
    houses[current_loc] = 1

    if toggle:
        santa_loc = ops[dir](santa_loc)
        houses_split[santa_loc] = 1
    else:
        robot_loc = ops[dir](robot_loc)
        houses_split[robot_loc] = 1
    toggle = not toggle

print 'Number of houses with at least one package: %d' % len(houses)
print 'Number of houses with at least one package (split): %d' % len(houses_split)

