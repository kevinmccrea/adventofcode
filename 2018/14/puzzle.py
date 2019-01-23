#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

input = int(data[0])

recipes = [3, 7]
pos = [0,1]

while len(recipes) < input + 10:

    combined = recipes[pos[0]] + recipes[pos[1]]
    if combined >= 10:
        recipes.append(1)
        recipes.append(combined % 10)
    else:
        recipes.append(combined)

    pos = [(p+recipes[p]+1) % len(recipes) for p in pos]

print recipes[-10:]

recipes = [3, 7]
pos = [0,1]
done = False
#input_list = map(int, '01245')
input_list = map(int, str(input))
while not done:

    combined = recipes[pos[0]] + recipes[pos[1]]
    if combined >= 10:
        recipes.append(1)
        recipes.append(combined % 10)
    else:
        recipes.append(combined)

    pos = [(p+recipes[p]+1) % len(recipes) for p in pos]

    if len(recipes)> 6:
        #if recipes[-6:] == map(int, '51589'):
        #print len(recipes), recipes[-6:], input_list
        if recipes[-len(input_list):] == input_list or recipes[-len(input_list)-1:-1] == input_list:
            print len(recipes) - len(input_list)
            done = True

print recipes[-10:]

