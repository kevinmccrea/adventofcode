#!/usr/bin/env python

import sys
import md5

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

salt = 'abc'
salt = 'jlmsuwbz'
index = 0
hashes = []
keys = []
done = False

for ii in xrange(1000):
    #hashes.append(md5.new(salt + str(index+ii)).hexdigest())
    st_hash = md5.new(salt + str(index+ii)).hexdigest()
    for ii in xrange(2016):
        st_hash = md5.new(st_hash).hexdigest()
    hashes.append(st_hash)

print hashes[18]
print hashes[17]

while not done:
    #hashes.append(md5.new(salt + str(index+1000)).hexdigest())
    st_hash = md5.new(salt + str(index+1000)).hexdigest()
    for ii in xrange(2016):
        st_hash = md5.new(st_hash).hexdigest()
    hashes.append(st_hash)

    found = False
    attempted = False
    for ii in xrange(len(hashes[0])-2):
        if attempted:
            break
        if len(set(hashes[0][ii:ii+3])) == 1:
            attempted = True
            for hi in xrange(len(hashes[1:])):
                #if h.find(hashes[0][ii] * 5) >= 0:
                if hashes[1:][hi].find(hashes[0][ii] * 5) >= 0:
                    print hashes[0], '  found at ', index+1+hi, hashes[1:][hi], '   ', hashes[0][ii],  '  offset: ', hi
                    found = True

    if found:
        print 'index: ', index, ' hash: ', hashes[0]
        keys.append(hashes[0])
    
    if len(keys) == 64:
        done = True

    index += 1
    hashes = hashes[1:]

print len(hashes)
print index-1
