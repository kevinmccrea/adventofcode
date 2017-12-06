#!/usr/bin/env python
import math

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
max_rt = math.ceil(math.sqrt(value))
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




