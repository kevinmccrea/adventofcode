#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

class node:
    def __init__(self):
        self.name = ''
        self.cost = 0
        self.children = []

    def __str__(self):
        return self.name + " " +  str(self.cost) + " " + str(self.children)

def sum_cost(node, all_nodes):
    sum = all_nodes[node].cost
    for nn in all_nodes[node].children:
        sum += sum_cost(nn, all_nodes)

    return sum

def traverse(node, all_nodes, unbalanced):
    if len(all_nodes[node].children):
        if len(set([sum_cost(nn, all_nodes) for nn in all_nodes[node].children])) > 1:
            unbalanced.append(node)
            for nn in all_nodes[node].children:
                traverse(nn, all_nodes, unbalanced)
    return

nodes = {}
for line in data:
    parts = line.split('->')
    name = parts[0].split('(')[0].strip()
    cost = int(parts[0].split('(')[1].split(')')[0])
    children = []
    if len(parts) > 1:
        children = parts[1].split(',')
    
    item = node()
    item.name = name
    item.cost = cost
    item.children = map(str.strip, children)

    nodes[name] = item

root = nodes.keys()
# a nodes children can not be the root node
for node in nodes:
    for child in nodes[node].children:
        root.remove(child)

print root
print nodes[root[0]].name, nodes[root[0]].cost

for ii in xrange(len(nodes[root[0]].children)):
    print str(nodes[nodes[root[0]].children[ii]].cost) + ' '

print nodes[root[0]]
print nodes[nodes[root[0]].children[0]]

unbal = []
traverse(root[0], nodes, unbal)
print "unbalanced"
print nodes[unbal[-1]]
print "cost: ", nodes[unbal[-1]].cost
for nn in nodes[unbal[-1]].children:
    print nn, sum_cost(nn, nodes)

print nodes['fabacam']
