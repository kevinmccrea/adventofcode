#!/usr/bin/env python

import sys
import operator

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

sector_id_sum = 0
valid_rooms = []
for line in data:
    line.strip()
    
    code = line.split('-')[:-1]
    sector_id = line.split('-')[-1].split('[')[0]
    check_sum = line.split('-')[-1].split('[')[1][:-2]

    counts = {}
    for word in code:
        for letter in word:
            if counts.has_key(letter):
                counts[letter] += 1
            else:
                counts[letter] = 1

    valid = True

    sorts = sorted(counts.items(), key=operator.itemgetter(0))
    sorts = sorted(sorts, key=operator.itemgetter(1), reverse=True)
    
    #print sorts
    for xx in xrange(len(check_sum)):
        if sorts[xx][0] != check_sum[xx]:
            valid = False

    if valid:
        sector_id_sum += int(sector_id)
        valid_rooms.append((code, sector_id))

for line in valid_rooms:
    code = line[0]
    sector_id = line[1]

    enc = ' '.join(code)
    dec = ''.join(map(lambda c: chr(ord('a') + (ord(c) - ord('a') + int(sector_id))%26) if c != ' ' else c, enc))

    if dec.find('north') >= 0:
        print dec, sector_id

    #print dec

print sector_id_sum

