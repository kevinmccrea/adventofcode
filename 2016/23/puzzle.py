#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = [line.strip() for line in data]

ip = 0

REGS = {'a':7, 'b':0, 'c':0, 'd':0}
REGS = {'a':12, 'b':0, 'c':0, 'd':0}

def print_inst(data, ip):
    print '########################'
    for xx in xrange(len(data)):
        print data[xx],
        if ip == xx:
            print '<<<<'
        else:
            print ' '

while ip >= 0 and ip < len(data):

    #print_inst(data, ip)

    inst = data[ip].strip()

    #print inst, REGS['a'], REGS['b'], REGS['c'], REGS['d']

    if inst.startswith('cpy'):
        (trash, op1, reg) = inst.split()

        if op1 in REGS.keys():
            val = REGS[op1]
        else:
            val = int(op1)

        if reg in REGS.keys():
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
            if offset in REGS.keys():
                ip += REGS[offset]
            else:
                ip += int(offset)
        else:
            ip += 1

    elif inst.startswith('tgl'):
        op1 = inst.split()[1]
        if op1 in REGS.keys():
            val = REGS[op1]
        else:
            val = int(op1)

        ind = ip + val
        if ind >= 0 and ind < len(data):
            tokens = data[ind].split()
            tinst = tokens[0]
            if len(tokens) == 2:
                if tokens[0] == 'inc':
                    tokens[0] = 'dec'
                else:
                    tokens[0] = 'inc'
            else:
                if tokens[0] == 'jnz':
                    tokens[0] = 'cpy'
                else:
                    tokens[0] = 'jnz'

            orig = data[ind]
            data[ind] = ' '.join(tokens)
        
            #print 'TGL', orig, ' ----> ', data[ind]
        ip += 1
    elif inst.startswith('mul'):
        _, a, b, reg = inst.split()
        REGS[reg] = REGS[a] * REGS[b]
        ip += 1
    elif inst.startswith('#'):
        ip += 1
    else:
        print 'ERROR ', inst

    toggles = [inst for inst in data if inst.startswith('tgl')]
    if not len(toggles):
        print 'PROGRAM  ip(%d)' % ip
        for line in data:
            print line
        sys.exit()

print REGS['a']
