#!/usr/bin/env python

import sys
import collections
import itertools

import aoc

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = [line.strip() for line in data]

ops = map(int, data[0].split(','))

def run_code(ops, noun, verb):
    regs = collections.defaultdict(int)
    for ii in xrange(len(ops)):
        regs[ii] = ops[ii]

    regs[1] = noun
    regs[2] = verb

    pc = 0
    done = False
    while not done:
        op = regs[pc]
        if op == 1:
            x = regs[pc+1]
            y = regs[pc+2]
            out = regs[pc+3]
            regs[out] = regs[x] + regs[y]
        elif op == 2:
            x = regs[pc+1]
            y = regs[pc+2]
            out = regs[pc+3]
            regs[out] = regs[x] * regs[y]
        elif op == 99:
            done = True
        else:
            print op
            print "yikes"
            sys.exit(1)

        pc += 4

    return regs[0]

print 'Part 1:', run_code(ops, 12, 2)

for x in xrange(99):
    for y in xrange(99):
        val = run_code(ops, x, y)
        if val == 19690720:
            print 100 * x + y
            sys.exit(1)
