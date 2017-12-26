#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

groups = []
for line in data:
    target = line.split()[0]
    peers = map(str.strip, line.split('>')[1].split(','))

    all_nodes = [target]
    all_nodes.extend(peers)

    # find the sets to merge
    merge_sets = []
    for node in all_nodes:
        for g in groups:
            if node in g:
                merge_sets.append(g)

    if len(merge_sets) > 0:
        new_set = set(all_nodes)
        for s in merge_sets:
            new_set |= s
            if s in groups:
                groups.remove(s)

        groups.append(new_set)
        
    else:
        # create a new set
        groups.append(set(all_nodes))


#print groups
for s in groups:
    if '0' in s:
        print "Part 1: %d" % len(s)

print "Part 2: %d" % len(groups)
