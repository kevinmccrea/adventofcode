#!/usr/bin/env python

import sys
import collections
import itertools
import numpy

import aoc

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = [line.strip() for line in data]

def swap(arg, ind1, ind2):
    print 'swap', arg, ind1, ind2
    temp = arg[ind1]
    arg[ind1] = arg[ind2]
    arg[ind2] = temp
    print arg

def swap_char(arg, char1, char2):
    print 'swapchar', arg, char1, char2
    ind1 = numpy.where(arg == char1)[0][0]
    ind2 = numpy.where(arg == char2)[0][0]

    swap(arg, ind1, ind2)
    print arg

def rotate_int(arg, x):
    print 'rotate', arg, x
    numpy.put(arg, range(len(arg)), numpy.roll(arg, x))
    print arg

def rotate_char(arg, ch):
    print 'rotate_char', arg, ch
    ind = numpy.where(arg == ch)[0][0]
    if ind >= 4:
        count = ind + 2
    else:
        count = ind + 1
    rotate_int(arg, count)
    print arg

def unrotate_char(arg, ch):
    done = False
    curr = numpy.array(arg)
    rotate_int(curr, 1)
    while not done:
        temp = numpy.array(curr)
        rotate_char(temp, ch)
        if numpy.array_equal(temp, arg):
            done = True
        else:
            rotate_int(curr, 1)

    numpy.put(arg, range(len(arg)), curr)

def reverse(arg, ind1, ind2):
    print 'reverse', arg, ind1, ind2
    sub = arg[ind1:ind2+1][:]
    numpy.put(arg, range(ind1,ind2+1), sub[::-1])
    print arg

def move(arg, ind1, ind2):
    print 'move', arg, ind1, ind2
    ch = arg[ind1]
    if ind1 < ind2:
        sub = numpy.array(arg[ind1+1:ind2+2])
        numpy.put(arg, range(ind1,ind2+1), sub)
    elif ind2 < ind1:
        sub = numpy.array(arg[ind2:ind1])
        numpy.put(arg, range(ind2+1, ind1+1), sub)
    arg[ind2] = ch

password = numpy.array(list('abcdefgh'))
#password = numpy.array(list('abcde'))

for line in data:
    tokens = line.split()
    if line.startswith('swap position'):
        swap(password, int(tokens[2]), int(tokens[5]))
    elif line.startswith('swap letter'):
        swap_char(password, tokens[2], tokens[5])
    elif line.startswith('rotate left'):
        rotate_int(password, -int(tokens[2]))
    elif line.startswith('rotate right'):
        rotate_int(password, int(tokens[2]))
    elif line.startswith('rotate based'):
        rotate_char(password, tokens[6])
    elif line.startswith('reverse positions'):
        reverse(password, int(tokens[2]), int(tokens[4]))
    elif line.startswith('move position'):
        move(password, int(tokens[2]), int(tokens[5]))
    else:
        print 'ERROR', line

print 'Part 1:', ''.join(password)

password = numpy.array(list('fbgdceah'))

for line in data[::-1]:
    tokens = line.split()
    if line.startswith('swap position'):
        swap(password, int(tokens[2]), int(tokens[5]))
    elif line.startswith('swap letter'):
        swap_char(password, tokens[5], tokens[2])
    elif line.startswith('rotate left'):
        rotate_int(password, int(tokens[2]))
    elif line.startswith('rotate right'):
        rotate_int(password, -int(tokens[2]))
    elif line.startswith('rotate based'):
        unrotate_char(password, tokens[6])
    elif line.startswith('reverse positions'):
        reverse(password, int(tokens[2]), int(tokens[4]))
    elif line.startswith('move position'):
        move(password, int(tokens[5]), int(tokens[2]))
    else:
        print 'ERROR', line

print 'Part 2:', ''.join(password)
