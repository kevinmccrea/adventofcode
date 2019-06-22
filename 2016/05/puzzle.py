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

door_id = data[0].strip()

done = False
num_found = 0
index = 0
password = list('________')
hashes = []
while not done:
    
    ans = md5.new(str(door_id + str(index))).hexdigest()
    
    if len(ans) > 5 and ans[:5] == '00000':
        hashes.append(ans)
        try:
            pos = int(ans[5])
        except:
            pos = 10
        print 'testing: ', ans, '  ', pos
        if pos < 8 and password[pos] == '_':
            num_found += 1
            password[pos] = ans[6]
            print 'found', ans

    if num_found == 8:
        done = True

    index+=1

print ''.join(password)
