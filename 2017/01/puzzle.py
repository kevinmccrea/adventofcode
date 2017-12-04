#!/usr/bin/env python

f = open('input.txt', 'r')
data = f.readline().strip()
f.close()

#data = '91212129'
total1 = 0
total2 = 0
input = data

length = len(input)
for ii in xrange(len(input)):
    if input[ii] == input[(ii+1) % length]:
        total1 += int(input[ii])
    if input[ii] == input[(ii+length/2) % length]:
        total2 += int(input[ii])

print total1
print total2

