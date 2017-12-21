#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

def dist(p0,p1):
    return abs(p1[0]) + abs(p1[1]) + abs(p1[2])
    #return math.sqrt((p1[0]-p0[0])**2 + (p1[1]-p0[1])**2 + (p1[2]-p0[2])**2)

class particle:
    def __init__(self, p, v, a):
        self.pos = p
        self.vel = v
        self.acc = a
        
        self.zero_dist = dist((0,0,0), p)
        self.zero_vel = 0

        self.destroyed = False

    def __str__(self):
        return "p%s v%s a%s  dist: %d" % (self.pos, self.vel, self.acc, self.zero_dist) 

    def step(self):
        self.vel = tuple([self.vel[ii] + self.acc[ii] for ii in xrange(3)])
        self.pos = tuple([self.pos[ii] + self.vel[ii] for ii in xrange(3)])

        new_dist = dist((0,0,0), self.pos)
        self.zero_vel = new_dist - self.zero_dist
        self.zero_dist = new_dist


parts = []
for line in data:
    els = [tuple(map(int, el[2:].replace('<',' ').replace('>', ' ').replace(',',' ').split())) for el in line.split(' ')]
    print els
    parts.append(particle(els[0], els[1],els[2]))

print len(parts)
print parts[0].pos

while True:
#for ss in xrange(4):
    for ii in xrange(len(parts)):
        parts[ii].step()
        #print ii, parts[ii].zero_dist

    for ii in xrange(len(parts)-1):
        ref = parts[ii].pos
        for xx in xrange(ii+1, len(parts)):
            if ref == parts[xx].pos:
                parts[ii].destroyed = True
                parts[xx].destroyed = True
    parts = [pp for pp in parts if not pp.destroyed]

    min_index = 0
    min_value = parts[0].zero_dist
    for ii in xrange(len(parts)):
        if parts[ii].zero_dist < min_value:
            min_value = parts[ii].zero_dist
            min_index = ii

    #print '################### Step %d ########################' % ss
    #for p in parts:
    #    print p
    
    print "Num alive: %d    Min: %d" % (len(parts),min_index)
