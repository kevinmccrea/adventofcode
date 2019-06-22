#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

tls = 0
for line in data:
    line = line.strip()
    
    in_subnet = 0
    valid = True
    found = False
    for ii in xrange(len(line)-3):
        if line[ii] == '[':
            in_subnet += 1
            continue
        if line[ii] == ']' and in_subnet > 0:
            in_subnet -= 1
            continue

        if line[ii] == line[ii+3] and line[ii+1] == line[ii+2] and line[ii] != line[ii+1]:
            if in_subnet:
                valid = False
            else:
                found = True

    if valid and found:
        tls += 1

print tls

num = 0
for line in data:
    line = line.strip()

    addrs = []
    subnets = []

    curr_field = []
    for char in list(line):
        if char == '[':
            if len(curr_field):
                addrs.append(''.join(curr_field))
            curr_field = []
        elif char == ']':
            if len(curr_field):
                subnets.append(''.join(curr_field))
            curr_field = []
        else:
            curr_field.append(char)

    if len(curr_field):
        addrs.append(''.join(curr_field))

    valid = True
    found = False
    for addr in addrs:
        for ii in xrange(len(addr)-2):
            if addr[ii] == addr[ii+2] and addr[ii] != addr[ii+1]:
                for sub in subnets:
                    if sub.find(addr[ii+1]+addr[ii]+addr[ii+1]) >=0:
                        found = True
    
    if valid and found:
        num += 1


print num
