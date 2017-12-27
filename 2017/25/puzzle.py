#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

class Tape:
    def __init__(self, max_steps):
        self.tape = [0] * (max_steps * 2 + 1)
        self.curr_index = max_steps
        self.min_index = max_steps
        self.max_index = max_steps

    def get(self):
        return self.tape[self.curr_index]

    def write_and_shift(self, val, shift):
        self.tape[self.curr_index] = val

        self.curr_index += shift
        if self.curr_index < self.min_index:
            self.min_index = self.curr_index
        if self.curr_index > self.max_index:
            self.max_index = self.curr_index

def A(tape):
    if tape.get() == 0:
        tape.write_and_shift(1, 1)
        return 'B'
    else:
        tape.write_and_shift(0, -1)
        return 'C'

def B(tape):
    if tape.get() == 0:
        tape.write_and_shift(1, -1)
        return 'A'
    else:
        tape.write_and_shift(1, 1)
        return 'D'

def C(tape):
    if tape.get() == 0:
        tape.write_and_shift(0, -1)
        return 'B'
    else:
        tape.write_and_shift(0, -1)
        return 'E'

def D(tape):
    if tape.get() == 0:
        tape.write_and_shift(1, 1)
        return 'A'
    else:
        tape.write_and_shift(0, 1)
        return 'B'

def E(tape):
    if tape.get() == 0:
        tape.write_and_shift(1, -1)
        return 'F'
    else:
        tape.write_and_shift(1, -1)
        return 'C'

def F(tape):
    if tape.get() == 0:
        tape.write_and_shift(1, 1)
        return 'D'
    else:
        tape.write_and_shift(1, 1)
        return 'A'

ops = {'A':A,
       'B':B,
       'C':C,
       'D':D,
       'E':E,
       'F':F}

steps = 12481997
tape = Tape(steps)
curr_state = 'A'
for ii in xrange(steps):
    next_state = ops[curr_state](tape)

    curr_state = next_state

print 'Part 1: num ones %d' % tape.tape.count(1)
