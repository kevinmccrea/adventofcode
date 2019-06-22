#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

ip = 0

REGS = {'a':0, 'b':0, 'c':0, 'd':0}
REGS = {'a':0, 'b':0, 'c':1, 'd':0}

while ip < len(data):
    inst = data[ip].strip()

    #print inst, REGS['a'], REGS['b'], REGS['c'], REGS['d']

    if inst.startswith('cpy'):
        (trash, op1, reg) = inst.split()

        if op1 in REGS.keys():
            val = REGS[op1]
        else:
            val = int(op1)

        REGS[reg] = val

        ip += 1

    elif inst.startswith('inc'):
        (trash, reg) = inst.split()

        REGS[reg] += 1

        ip += 1

    elif inst.startswith('dec'):
        (trash, reg) = inst.split()

        REGS[reg] -= 1
        
        ip += 1

    elif inst.startswith('jnz'):
        (trash, op1, offset) = inst.split()
        if op1 in REGS.keys():
            val = REGS[op1]
        else:
            val = int(op1)

        if val:
            ip += int(offset)
        else:
            ip += 1

    else:
        print 'fuck ', inst

print REGS['a']
