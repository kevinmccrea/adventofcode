#!/usr/bin/env python

import sys
import collections
import itertools

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()
data = [line.strip() for line in data]

data = map(int, data[0].split())

all_meta = []
def create_node(tree, ss):
    global all_meta

    num_children = ss.pop(0)
    num_meta = ss.pop(0)
    node = {}
    node['id'] = len(tree.keys())
    node['children'] = []
    for ii in xrange(num_children):
        node['children'].append(create_node(tree, ss))
    node['meta'] = [ss.pop(0) for m in xrange(num_meta)]
    all_meta.extend(node['meta'])

    node['value'] = 0
    if num_children == 0:
        node['value'] += sum(node['meta'])
    else:
        for mm in node['meta']:
            if mm > 0 and mm <= len(node['children']):
                node['value'] += node['children'][mm-1]['value']

    return node

tree = create_node({}, data)

print sum(all_meta)

print tree['value']
