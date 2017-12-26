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


def knot_hash(data, lens):
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

    return data

data = data[0].strip()
lens = map(int, data.split(','))
string = [xx for xx in xrange(256)]

#lens = [3,4,1,5]
#string = [xx for xx in xrange(5)]

string = hash(string, lens)
print 'Part 1: %d (%d * %d)' % (string[0]*string[1], string[0], string[1])

lens = [ord(ch) for ch in data] + [17,31,73,47,23]
lens = lens * 64
string = [xx for xx in xrange(256)]
sparse_hash = hash(string, lens)
dense_hash = [reduce(operator.xor, sparse_hash[ii:ii+16]) for ii in xrange(0,len(sparse_hash),16)]
print 'Part 2: %s' % binascii.hexlify(bytearray(dense_hash))

