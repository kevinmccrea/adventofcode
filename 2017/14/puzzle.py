#!/usr/bin/env python

import sys
import operator
import binascii

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

#
# Copied from Day 10
#
def knot_hash(hash_string):

    data = [xx for xx in xrange(256)]
    lens = [ord(ch) for ch in hash_string] + [17,31,73,47,23]
    lens = lens * 64

    skip_size = 0
    curr_pos = 0
    for run_length in lens:
        # extend the list to handle wrap-around
        working = data + data

        # twist the portion
        working = working[0:curr_pos] + working[curr_pos:curr_pos + run_length][::-1] + working[curr_pos+run_length:]
        
        # extract the twisted portion
        if curr_pos + run_length > len(data):
            num_wrapped = (curr_pos + run_length) % len(data)
            data = working[len(data):len(data)+num_wrapped] + working[num_wrapped:len(data)]
        else:
            data = working[0:len(data)]

        curr_pos = (curr_pos + run_length + skip_size) % len(data)

        skip_size += 1

    sparse_hash = data
    dense_hash = [reduce(operator.xor, sparse_hash[ii:ii+16]) for ii in xrange(0,len(sparse_hash),16)]

    return  binascii.hexlify(bytearray(dense_hash))

def get_adj_regions(disk, x, y):
    regions = set()
    if x > 0 and disk[x-1][y] != 0:
        regions.add(disk[x-1][y])

    if y > 0 and disk[x][y-1] != 0:
        regions.add(disk[x][y-1])

    return list(regions)

def replace_region(disk, old, new):
    for row in xrange(len(disk)):
        for col in xrange(len(disk[row])):
            if disk[row][col] == old:
                disk[row][col] = new
    #for sector in disk:
    #    sector = [new if x == old else x for x in sector]

salt = data[0].strip()

#salt = 'flqrgnkx'
hashes = [knot_hash(salt+'-'+str(ii)) for ii in xrange(128)]

bits_set = 0
disk = []
for hash in hashes:
    sector = ''
    for ch in hash:
        sector += format(int(ch,16), '04b')
    bits_set += sector.count('1')
    disk.append([int(ch) for ch in sector])

print 'Part 1: total bits set %d' % bits_set

groups = set()
next_group = 2
for row in xrange(len(disk)):
    for col in xrange(len(disk[row])):
        if disk[row][col] == 1:
            adj = get_adj_regions(disk, row, col)
            if len(adj) == 0:
                disk[row][col] = next_group;
                groups.add(next_group)
                next_group += 1
            elif len(adj) == 1:
                disk[row][col] = adj[0]
            elif len(adj) == 2:
                replace_region(disk, adj[1], adj[0])
                disk[row][col] = adj[0]
                groups.remove(adj[1])
            else:
                print 'ERROR'

print 'Part 2: num regions %d' % len(groups)

