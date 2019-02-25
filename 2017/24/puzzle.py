#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

all_ports = []
all_pins = set()
for line in data:
    x,y = map(int, line.strip().split('/'))
    all_pins.add(x)
    all_pins.add(y)
    all_ports.append((x,y))

port_map = {}
for pin in all_pins:
    ports = []
    for port in all_ports:
        if pin in port:
            ports.append(port)
    port_map[pin] = ports

def find_chains(completed, curr_chain, curr_pin, remaining_ports):
    choices = [xx for xx in remaining_ports if curr_pin in xx]
    if len(choices) == 0:
        completed.append(curr_chain[:])
        return

    for choice in choices:
        new_chain = curr_chain[:]
        new_chain.append(choice)
        new_remaining = remaining_ports[:]
        new_remaining.remove(choice)
        new_pin = choice[0] if choice[0] != curr_pin else choice[1]
        find_chains(completed, new_chain, new_pin, new_remaining)

    return

completed = []
find_chains(completed, [], 0, all_ports[:])

print len(completed)
max_sum = 0
max_length = 0
max_length_sum = 0
for chain in completed:
    curr_sum = 0
    for port in chain:
        curr_sum += port[0] + port[1]

    if curr_sum > max_sum:
        max_sum = curr_sum

    if len(chain) > max_length:
        max_length = len(chain)
        max_length_sum = curr_sum
    elif len(chain) == max_length and curr_sum >= max_length_sum:
        max_length_sum = curr_sum


print 'Part 1: strongest %d' % max_sum
print 'Part 2: strongest longest %d' % max_length_sum

