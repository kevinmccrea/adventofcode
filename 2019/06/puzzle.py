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


orbits = {}
for line in data:
    a, b = line.split(')')
    # b orbits a
    orbits[b] = a

def count_orbits(orbits, target):
    if target not in orbits:
        return 0

    num = 1
    key = target
    next = orbits[key]
    while next in orbits:
        num+=1
        next = orbits[next]

    return num

def count_all(orbits):
    num = 0
    for key in orbits.keys():
        num += count_orbits(orbits, key)
    return num

print 'Part 1:', count_all(orbits)

def follow_orbits(orbits, target):
    all = []
    curr = target
    while curr in orbits:
        all.append(orbits[curr])
        curr = orbits[curr]
    return all

you_path = follow_orbits(orbits, 'YOU')
san_path = follow_orbits(orbits, 'SAN')

common = list(set(you_path).intersection(set(san_path)))

common_counts = [count_orbits(orbits, c) for c in common]

high_c = common_counts[0]
target_p = common[0]
for p, c in zip(common, common_counts):
    if c > high_c:
        target_p = p
        high_c = c

common_count = count_orbits(orbits, target_p)
you_count = count_orbits(orbits, 'YOU')
san_count = count_orbits(orbits, 'SAN')

print 'Part 2:', (you_count - 1 - common_count) + (san_count - 1 - common_count)

