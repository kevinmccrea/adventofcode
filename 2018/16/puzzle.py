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

data1 = data[:3144]
data2 = data[3145:]

ops = ['addr', 'addi', 'mulr','muli','banr','bani','borr','bori','setr','seti','gtir','gtri','gtrr','eqir','eqri','eqrr']

regs = (0,0,0,0)

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

samples = []
op_sets = {}
counts = 0
for ii in xrange(3145/4):
    samp = data1[ii*4:ii*4+5]
    before = tuple(map(int, samp[0].split('[')[1][0:-1].split(',')))
    inst = tuple(map(int, samp[1].split()))
    after = tuple(map(int, samp[2].split('[')[1][0:-1].split(',')))

    curr = [op for op in ops if after == run_op((op, inst[1], inst[2], inst[3]), before)]
    print inst[0], curr
    
    if op_sets.has_key(inst[0]):
        op_sets[inst[0]] = op_sets[inst[0]] & set(curr)
    else:
        op_sets[inst[0]] = set(curr)

    if len(curr) >= 3:
        counts += 1

    samples.append(curr)

print counts

print op_sets

ops = {}
while op_sets.keys():
    removed = []
    for k, v in op_sets.items():
        if len(list(v)) == 1:
            ops[k] = list(v)[0]
            removed.append(list(v)[0])
            del op_sets[k]
    for k,v in op_sets.items():
        op_sets[k] -= set(removed)

print ops

regs=(0,0,0,0)
for line in data2:
    if not line.strip():
        continue

    inst = map(int, line.split())
    inst[0] = ops[inst[0]]
    #print inst
    regs = run_op(inst, regs)

print regs[0]


