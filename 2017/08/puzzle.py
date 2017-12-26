#!/usr/bin/env python

import sys
import collections
import operator

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

def deref(regs, val):
    try:
        ret = int(val)
        return ret
    except:
        return int(regs[val])

regs = collections.defaultdict(int)
conds = {'>': operator.gt,
         '<': operator.lt,
         '>=': operator.ge,
         '<=': operator.le,
         '==': operator.eq,
         '!=': operator.ne}

max_ever = 0
for line in data:
    (reg, op, val, if_str, if_reg, cond, cond_val) = line.strip().split()

    if conds[cond](deref(regs, if_reg), deref(regs,cond_val)):
        if op == 'inc':
            regs[reg] += deref(regs, val)
            if regs[reg] > max_ever:
                max_ever = regs[reg]
        elif op == 'dec':
            regs[reg] -= deref(regs, val)
            if regs[reg] > max_ever:
                max_ever = regs[reg]
        else:
            print 'FAIL'
    
print 'Part 1: max val %d' % max(regs.values())
print 'Part 2: max ever %d' % max_ever
