#!/usr/bin/env python

import sys
import collections
import itertools

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = [line.strip() for line in data]

ip_reg = 5
ip = 0
data = data[1:]

ops = ['addr', 'addi', 'mulr','muli','banr','bani','borr','bori','setr','seti','gtir','gtri','gtrr','eqir','eqri','eqrr']

regs = (0,0,0,0,0,0)

def run_op(inst, regs):
    op,a,b,c = inst
    regs = list(regs)
    if op == 'addr':
        regs[c] = regs[a] + regs[b]
    elif op == 'addi':
        regs[c] = regs[a] + b
    elif op == 'mulr':
        regs[c] = regs[a] * regs[b]
    elif op == 'muli':
        regs[c] = regs[a] * b
    elif op == 'banr':
        regs[c] = regs[a] & regs[b]
    elif op == 'bani':
        regs[c] = regs[a] & b
    elif op == 'borr':
        regs[c] = regs[a] | regs[b]
    elif op == 'bori':
        regs[c] = regs[a] | b
    elif op == 'setr':
        regs[c] = regs[a]
    elif op == 'seti':
        regs[c] = a
    elif op == 'gtir':
        if a > regs[b]:
            regs[c] = 1
        else:
            regs[c] = 0
    elif op == 'gtri':
        if regs[a] > b:
            regs[c] = 1
        else:
            regs[c] = 0
    elif op == 'gtrr':
        if regs[a] > regs[b]:
            regs[c] = 1
        else:
            regs[c] = 0
    elif op == 'eqir':
        if a == regs[b]:
            regs[c] = 1
        else:
            regs[c] = 0
    elif op == 'eqri':
        if regs[a] == b:
            regs[c] = 1
        else:
            regs[c] = 0
    elif op == 'eqrr':
        if regs[a] == regs[b]:
            regs[c] = 1
        else:
            regs[c] = 0
    else:
        print 'error', op
        sys.exit()
    return tuple(regs)

ip = regs[ip_reg]
while ip >= 0 and ip < len(data):
    #ip = regs[ip_reg]
    line = data[ip]

    op = line.split()[0]
    a,b,c = map(int, line.split()[1:])
    inst = (op, a, b, c)
    
    lregs = list(regs)
    lregs[ip_reg] = ip
    regs = tuple(lregs)

    #print ip, regs, 
    regs = run_op(inst, regs)
    ip = regs[ip_reg] + 1

    #print inst, regs
    
print regs
