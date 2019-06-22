#!/usr/bin/env python

import numpy

f = open('input.txt', 'r')
data = f.readlines()
f.close()

dirs = [[-1,0], [0,1], [1,0], [0,-1]]

nums = [[1,2,3], [4,5,6], [7,8,9]]

nums2 = [['x','x','1','x','x'],['x','2','3','4','x'],['5','6','7','8','9'],['x','A','B','C','x'],['x','x','D','x','x']]
#data=["ULL","RRDDD","LURDL","UUUUD"]

dir_inds = {'U':0, 'R':1, 'D':2, 'L':3}
start_button = numpy.array([2,0])
code=[]
for line in data:
    for ii in xrange(len(line.strip())):
        move = numpy.array(dirs[dir_inds[line[ii]]])
        print move 
        new_button = move+start_button

        
        #if len([1 for val in new_button if val < 0 or val > 2]):
        if len([1 for val in new_button if val < 0 or val > 4]) or nums2[new_button[0]][new_button[1]] == 'x':
            #print 'nope'
            #print numpy.where(new_button < 0).sum(), numpy.where(new_button > 3)
            print line[ii], 'ERROR'
            continue

        start_button = new_button
    
        digit = nums2[start_button[0]][start_button[1]]
        print line[ii], '  at ', digit
    
    digit = nums2[start_button[0]][start_button[1]]
    code.append(digit)
        

    print start_button, nums2[start_button[0]][start_button[1]]


print code

