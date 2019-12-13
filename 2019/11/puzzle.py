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

def run_code(regs, inputs, outputs, pc=0,rel_base=0,output_yield=False):

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
            # rel_base set
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

class Computer:
    def __init__(self, code):
        self.pc = 0
        self.rel_base = 0
        self.inputs = []
        self.outputs = []

        self.is_halted = False

        self.code = code[:] + [0] * 10000
   
    def run(self):

        if self.is_halted:
            return

        (rc, pc, rb) = run_code(self.code, self.inputs, 
                self.outputs, self.pc, self.rel_base, True)

        self.pc = pc
        self.rel_base = rb

        if rc == 0:
            self.is_halted = True

        return 


def paint(ops, start_color):
    comp = Computer(ops)
    ship = {}
    cur_pos = (0,0)
    dirs = [(-1,0), (0,1), (1, 0), (0,-1)]
    cur_dir_ind = 0

    p_once = 0
    comp.inputs.append(start_color)
    while not comp.is_halted:
        comp.run()
        
        if comp.is_halted:
            break

        color = comp.outputs.pop(0)
        
        comp.run()
        
        direction = comp.outputs.pop(0)

        # paint
        if cur_pos not in ship:
            p_once += 1

        ship[cur_pos] = color

        # turn
        if direction == 0:
            cur_dir_ind -= 1
        else:
            cur_dir_ind += 1
        cur_dir_ind %= 4

        # move
        cur_pos = aoc.tup_add(cur_pos, dirs[cur_dir_ind])

        # prep input
        if cur_pos in ship:
            comp.inputs.append(ship[cur_pos])
        else:
            comp.inputs.append(0)

       
        #aoc.print_maze(ship_out, '.')
    return (ship, p_once)

ship, p_once = paint(ops, 0)
print 'Part 1:', p_once

ship, p_once = paint(ops, 1)
for k in ship.keys():
    if ship[k] == 0:
        ship[k] = ' '
    if ship[k] == 1:
        ship[k] = '#'
aoc.print_maze(ship, '.')


