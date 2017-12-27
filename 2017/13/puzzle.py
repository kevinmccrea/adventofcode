#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

layers = {}
for line in data:
    tokens = map(str.strip, line.split(':'))
    layers[int(tokens[0])] = int(tokens[1])

#layers = {0:3,1:2,4:4,6:4}

def route_packet(layers, start_time=0):
    max_layer = max(layers.keys())
    severity = 0
    time = start_time
    layer = 0
    caught = False
    while layer < max_layer+1:
        if layers.has_key(layer):
            depth = layers[layer]
            if time % ((depth - 1) * 2) == 0:
                #print 'Caught layer: %d at %d for %d' % (layer, time, depth)
                severity += depth * layer
                caught = True
        time += 1
        layer += 1
    
    return (caught, severity)

print 'Part 1: severity %d' % route_packet(layers)[1]

delay = 0
done = False
while not done:
    (caught, severity) = route_packet(layers, delay)
    if not caught:
        done = True
    else:
        delay += 1

print 'Part 2: delay %d' % delay
