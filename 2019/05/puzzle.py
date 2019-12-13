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

def get_digit(number, n):
    return number // 10**n % 10

def decode(regs, x, mode):
    if mode == 0:
        val = regs[x]
    elif mode == 1:
        val = x
    else:
        print "mode unknown", mode

    return val

def run_code(ops, inputs, outputs):

    regs = ops[:]

    pc = 0
    done = False
    while not done:
        full_op = regs[pc]
        op = full_op % 100
        x_mode = get_digit(full_op, 2)
        y_mode = get_digit(full_op, 3)

        if op == 1:
            # Add
            x = regs[pc+1]
            y = regs[pc+2]
            out = regs[pc+3]

            x_val = decode(regs, x, x_mode)
            y_val = decode(regs, y, y_mode)

            regs[out] = x_val + y_val
            inc = 4
        elif op == 2:
            # Multiply
            x = regs[pc+1]
            y = regs[pc+2]
            out = regs[pc+3]
            
            x_val = decode(regs, x, x_mode)
            y_val = decode(regs, y, y_mode)
            
            regs[out] = x_val * y_val

            inc = 4
        elif op == 3:
            # Input
            if full_op != op:
                print 'yikes', full_op

            x = regs[pc+1]
            
            regs[x] = inputs.pop(0)

            inc = 2
        elif op == 4:
            # Output
            x = regs[pc+1]
            x_val = decode(regs, x, x_mode)

            outputs.append(x_val)

            inc = 2
        elif op == 5:
            # Jump if true
            x = regs[pc+1]
            y = regs[pc+2]
            x_val = decode(regs, x, x_mode)
            y_val = decode(regs, y, y_mode)
            
            if x_val:
                pc = y_val
                inc = 0
            else:
                inc = 3
        elif op == 6:
            # Jump if False
            x = regs[pc+1]
            y = regs[pc+2]
            x_val = decode(regs, x, x_mode)
            y_val = decode(regs, y, y_mode)
            
            if x_val == 0:
                pc = y_val
                inc = 0
            else:
                inc = 3
        elif op == 7:
            # Less than
            x = regs[pc+1]
            y = regs[pc+2]
            out = regs[pc+3]
            
            x_val = decode(regs, x, x_mode)
            y_val = decode(regs, y, y_mode)

            if x_val < y_val:
                regs[out] = 1
            else:
                regs[out] = 0
            
            inc = 4
        elif op == 8:
            # Equal
            x = regs[pc+1]
            y = regs[pc+2]
            out = regs[pc+3]
            
            x_val = decode(regs, x, x_mode)
            y_val = decode(regs, y, y_mode)

            if x_val == y_val:
                regs[out] = 1
            else:
                regs[out] = 0
            
            inc = 4

        elif op == 99:
            done = True
            inc = 0
        else:
            print op
            print "yikes op", op
            sys.exit(1)

        pc += inc

    return

inputs = [1]
outputs = []
run_code(ops[:], inputs, outputs)

print 'Part 1:', outputs

inputs = [5]
outputs = []
run_code(ops[:], inputs, outputs)

print 'Part 2:', outputs

