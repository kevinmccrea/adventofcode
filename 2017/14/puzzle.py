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

salt = data[0].strip()

#salt = 'flqrgnkx'
disk = [knot_hash(salt+'-'+str(ii)) for ii in xrange(128)]

bits_set = 0
for block in disk:    
    for ch in block:
        bits_set += format(int(ch,16), '04b').count('1')

print 'Part 1: total bits set %d' % bits_set

