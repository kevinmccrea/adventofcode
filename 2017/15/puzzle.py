#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

start_a = int(data[0].split()[-1])
start_b = int(data[1].split()[-1])

class generator:
    def __init__(self, start_val, factor, modulo=1):
        self.value = start_val
        self.factor = factor
        self.modulo = modulo

    def step(self):
        done = False
        while not done:
            self.value = (self.value * self.factor) % 2147483647
            if self.value % self.modulo == 0:
                done = True
        return self.value

gen_a = generator(start_a, 16807,1)
gen_b = generator(start_b, 48271,1)
#gen_a = generator(65, 16807)
#gen_b = generator(8921, 48271)

score = 0
xx = 0
mask = 2**16-1
for xx in xrange(40000000):
    gen_a.step()
    gen_b.step()
    
    #print gen_a.value, gen_b.value
    if gen_a.value & mask == gen_b.value & mask:
        score += 1


print 'Part 1: score %d' % score

gen_a = generator(start_a, 16807,4)
gen_b = generator(start_b, 48271,8)

score = 0
xx = 0
for xx in xrange(5000000):
    gen_a.step()
    gen_b.step()
    
    #print gen_a.value, gen_b.value
    if gen_a.value & mask == gen_b.value & mask:
        score += 1

print 'Part 2: score %d' % score

