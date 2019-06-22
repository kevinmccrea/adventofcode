#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

line = data[0].strip()

output = []
while len(line):
    if line[0] == '(':
        end_index = line.find(')')
        marker = line[1:end_index]
        print marker
        print marker.split('x')
        (num_chars, iters) = map(int, marker.split('x'))
            
        for ii in xrange(iters):
            output.extend(list(line[end_index+1:end_index+1+num_chars]))

        line = line[end_index+1+num_chars:]
        print line
    else:
        output.append(line[0])
        line = line[1:]
        print line

def decoded_len(data):
    data_len = 0
    while len(data):
        if data[0] == '(':
            end_index = data.find(')')
            marker = data[1:end_index]
            (num_chars, iters) = map(int, marker.split('x'))

            data_len += iters * decoded_len(data[end_index+1:end_index+1+num_chars])

            data = data[end_index+1+num_chars:]
        else:
            data_len += 1
            data = data[1:]
    
    return data_len

print ''
print ''.join(output)
print len(output)


print '####'
print decoded_len(data[0].strip())

