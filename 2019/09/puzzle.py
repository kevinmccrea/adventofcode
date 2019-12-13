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

def decode(regs, x, mode, rel_base):
    if mode == 0:
        val = regs[x]
    elif mode == 1:
        val = x
    elif mode == 2:
        val = regs[x+rel_base]
    else:
        print "mode unknown", mode

    return val

def decode_out(x, mode, rel_base):
    if mode == 2:
        val = x + rel_base
    else:
        val = x
    return val

def run_code(ops, inputs, outputs, pc=0,rel_base=0,output_yield=False):

    regs = ops[:]
    regs += [0] * 10000

    rel_base = 0

    #pc = 0
    done = False
    while not done:
        full_op = regs[pc]
        op = full_op % 100
        x_mode = get_digit(full_op, 2)
        y_mode = get_digit(full_op, 3)
        z_mode = get_digit(full_op, 4)

        if op == 1:
            # Add
            x = regs[pc+1]
            y = regs[pc+2]
            out = regs[pc+3]

            out = decode_out(out, z_mode, rel_base)

            x_val = decode(regs, x, x_mode, rel_base)
            y_val = decode(regs, y, y_mode, rel_base)

            regs[out] = x_val + y_val
            inc = 4
        elif op == 2:
            # Multiply
            x = regs[pc+1]
            y = regs[pc+2]
            out = regs[pc+3]
            out = decode_out(out, z_mode, rel_base)
            
            x_val = decode(regs, x, x_mode, rel_base)
            y_val = decode(regs, y, y_mode, rel_base)
            
            regs[out] = x_val * y_val

            inc = 4
        elif op == 3:
            # Input
            x = regs[pc+1]
            out = decode_out(x, x_mode, rel_base)
            
            regs[out] = inputs.pop(0)

            inc = 2
        elif op == 4:
            # Output
            x = regs[pc+1]
            x_val = decode(regs, x, x_mode, rel_base)

            outputs.append(x_val)

            inc = 2

            # yield output
            if output_yield:
                return (1, pc+inc, rel_base)

        elif op == 5:
            # Jump if true
            x = regs[pc+1]
            y = regs[pc+2]
            x_val = decode(regs, x, x_mode, rel_base)
            y_val = decode(regs, y, y_mode, rel_base)
            
            if x_val:
                pc = y_val
                inc = 0
            else:
                inc = 3
        elif op == 6:
            # Jump if False
            x = regs[pc+1]
            y = regs[pc+2]
            x_val = decode(regs, x, x_mode, rel_base)
            y_val = decode(regs, y, y_mode, rel_base)
            
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
            out = decode_out(out, z_mode, rel_base)
            
            x_val = decode(regs, x, x_mode, rel_base)
            y_val = decode(regs, y, y_mode, rel_base)

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
            out = decode_out(out, z_mode, rel_base)
            
            x_val = decode(regs, x, x_mode, rel_base)
            y_val = decode(regs, y, y_mode, rel_base)

            if x_val == y_val:
                regs[out] = 1
            else:
                regs[out] = 0
            
            inc = 4

        elif op == 9:
            x = regs[pc+1]
            x_val = decode(regs, x, x_mode, rel_base)
            
            rel_base += x_val

            inc = 2

        elif op == 99:
            done = True
            inc = 0
        else:
            print op
            print "yikes op", op
            sys.exit(1)

        pc += inc

    return (0, pc, rel_base)

def run_sequence(ops, seq):
    inputs = [0]
    outputs = [0]
    for phase in seq:
        inputs = [phase, outputs[0]]
        outputs = []
        run_code(ops[:], inputs, outputs)
        
    return outputs[0]

def run_feedback(ops, seq):
    print 'feedback'
    curr_ops = [ops[:] for ii in xrange(len(seq))]
    rcs = [1] * len(seq)
    pcs = [0] * len(seq)
    rel_bases = [0] * len(seq)

    cur_index = 0
    inputs = [[phase] for phase in seq]
    outputs = [[] for phase in seq]

    inputs[0].append(0)

    while sum(rcs) != 0:
        (rc, pc, rb) = run_code(curr_ops[cur_index], inputs[cur_index], outputs[cur_index], pcs[cur_index], rel_bases[cur_index], True)
        rcs[cur_index] = rc
        pcs[cur_index] = pc
        rel_bases[cur_index] = rb

        next_index = (cur_index + 1) % len(seq)
        inputs[next_index].append(outputs[cur_index][-1])

        cur_index = next_index

    return outputs[-1][-1]



inputs = [1]
outputs = []
val = run_code(ops[:], inputs, outputs)
print val
print 'Part 1:', outputs

inputs = [2]
outputs = []
val = run_code(ops[:], inputs, outputs)
print 'Part 2:', outputs

