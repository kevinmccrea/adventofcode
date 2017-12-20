#!/usr/bin/env python

import sys
import collections

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

pc = 0
freq = 0
rec_freq = 0
while pc >= 0 and pc < len(data):
    ops = data[pc].split()
    #print ops

    offset = 1

    op = ops[0]
    if op == 'snd':
        freq = deref(regs, ops[1])
    elif op == 'set':
        regs[ops[1]] = deref(regs, ops[2])
    elif op == 'add':
        regs[ops[1]] += deref(regs, ops[2])
    elif op == 'mul':
        regs[ops[1]] *= deref(regs, ops[2])
    elif op == 'mod':
        regs[ops[1]] %= deref(regs, ops[2])
    elif op == 'rcv':
        if deref(regs, ops[1]) != 0:
            rec_freq = freq
            print rec_freq
            break

    elif op == 'jgz':
        if deref(regs, ops[1]) > 0:
            offset = deref(regs, ops[2])
    else:
        print 'ERROR'
        break

    pc += offset

    #print ops, regs

print rec_freq
        
