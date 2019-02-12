#!/usr/bin/env python

import sys
import collections
import itertools
import math

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = [line.strip() for line in data]

bots = []
for line in data:
    tokens = line.replace('=', ' ').replace('<', ' ').replace('>', ' ').replace(',', ' ').split()
    bots.append(((int(tokens[1]), int(tokens[2]), int(tokens[3])), int(tokens[5])))

sbots = sorted(bots, key=lambda x: x[1])

def dist(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1]) + abs(x[2]-y[2])

def tup_add(x,y):
    return tuple([xx+yy for xx,yy in zip(x,y)])

strong = sbots[-1]
inrange = [bot for bot in bots if dist(strong[0], bot[0]) <= strong[1]]

print 'Part one:', len(inrange)


OFFSETS = [[-1, -1, -1], [-1, 1, -1], [1, -1, -1], [1, 1, -1],
           [-1, -1, 1], [-1, 1, 1], [1, -1, 1], [1, 1, 1]]

def find_next_region(regions):
    """
    Find the regions in the list that are most dense.  Taking into account:
     - number of actual bots
     - number of possible bots
     - size
     - distance from 0,0,0
    """
    #s_regions = regions[:]
    s_regions = regions
    s_regions.sort(key=lambda t:t['origin_dist'])
    s_regions.sort(key=lambda t:t['parent_hits'], reverse=True)
    s_regions.sort(key=lambda t:t['hits'], reverse=True)
    return s_regions.pop(0)

def breakup_region(region):
    """
    Divides a region into 8 quadrants centered around the region center
    """
    regions = []
    for offset in OFFSETS:
        half_radius = int(region['radius']/2)
        new_center = tuple([x + (y * half_radius) for x,y in zip(region['center'], offset)])
        new_radius = int(math.ceil(float(region['radius']) / 2))
        regions.append({'center': new_center, 
                        'radius': new_radius, 
                        'hits': 0, 
                        'parent_hits': region['hits'],
                        'origin_dist': dist((0,0,0), new_center)})

    return regions

def bots_in_region(region, bots):
    """
    Returns the number of bots whose power intersects the region
    """
    center = region['center']
    radius = region['radius']
    count = 0
    for pos, power in bots:
        if dist(center, pos) - power <= 3*radius:
            count += 1
    return count



def compute_zero_crossing(bots, origin):
    count = 0
    for pos, power in bots:
        r = power
        d = dist(origin, pos)
        if d <= r:
            count += 1
    return count

def find_max_in_region(region, bots, radius):
    max_hits = 0
    max_pos = region['center']
    for offset in itertools.product(range(-radius, radius+1), repeat=3):
        pos = tup_add(region['center'], offset)
        hits = compute_zero_crossing(bots, pos)
        if hits >= max_hits:
            if hits > max_hits or (hits == max_hits and dist((0,0,0), pos) < dist((0,0,0), max_pos)):
                max_hits = hits
                max_pos = pos
        #print pos, hits, dist((0,0,0), pos)

    return (max_pos, max_hits)


origin = (0,0,0)

# find max extent of any bot in any dimension
bound = 0
for bot in bots:
    pos, power = bot
    if max(map(abs, pos)) > bound:
        bound = max(pos)

# create the default region
start_region = {'center': origin, 'radius': bound+1, 'parent_hits': 0}
start_region['hits'] = bots_in_region(start_region, bots)

smallest_radius = bound
regions = breakup_region(start_region)
done = False
iters = 0
while not done:
#for ii in xrange(700):
    new_region = find_next_region(regions)
    new_region['hits'] = bots_in_region(new_region, bots)
    regions.extend(breakup_region(new_region))
    if new_region['radius'] < smallest_radius:
        smallest_radius = new_region['radius']
        #print iters, new_region['radius'], new_region
        #print compute_zero_crossing(bots, new_region['center'])

    if new_region['radius'] == 1 and new_region['parent_hits'] == new_region['hits']:
        done = True
        #break
        
    iters += 1

print 'ITERS: ', iters, new_region

#print new_region
max_pos, max_hits = find_max_in_region(new_region, bots, 2)
print 'Part two: ', dist((0,0,0), max_pos)
