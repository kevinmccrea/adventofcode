#!/usr/bin/env python

import sys
import operator

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

maze = [list(line.strip('\n')) for line in data]

fixes = {'v': '|', '^':'|',
         '<': '-', '>':'-'}
init_dirs = {'v': (1,0), '^': (-1,0),
             '<': (0,-1), '>': (0,1)}
cart_markers = ['v','^','<','>']

turn_rots = [complex(0,1), complex(1,0), complex(0,-1)]

print len(maze), len(maze[0])
carts = []
for rr in xrange(len(maze)):
    for cc in xrange(len(maze[0])):
        #print rr, cc
        mark = maze[rr][cc]
        if mark in cart_markers:
            carts.append(((rr,cc),init_dirs[mark], 0))
            maze[rr][cc] = fixes[mark]

def add_tups(a,b):
    return (a[0]+b[0], a[1]+b[1])

def get_next(cart, mark):
    pos, prev_dir, rot_ind = cart
    if mark in ['|', '-']:
        next_dir = prev_dir
    elif mark == '/':
        next_dir = (prev_dir[1]*-1, prev_dir[0]*-1)
    elif mark == '\\':
        next_dir = (prev_dir[1], prev_dir[0])
    elif mark == '+':
        cpx_dir = complex(*prev_dir) * turn_rots[rot_ind]
        rot_ind = (rot_ind + 1) % len(turn_rots)
        next_dir = (int(cpx_dir.real), int(cpx_dir.imag))
    else:
        print 'ERROR', mark
        raise Exception("DD")

    new_pos = add_tups(pos, next_dir)
    
    return (new_pos, next_dir, rot_ind)

def is_collision(cart, carts):
    cols = [c for c in carts if c[0] == cart[0]]
    return len(cols) != 0

def print_maze(maze, carts):
    for rr in xrange(len(maze)):
        line = []
        for cc in xrange(len(maze[0])):
            if is_collision(((rr,cc), (0,0), 0), carts):
                line.append('X')
            else:
                line.append(maze[rr][cc])
        print ''.join(line)

print_maze(maze, carts)
print carts

done = False
tick = 0
while not done:

    carts.sort(key=lambda x: x[0][1])
    carts.sort(key=lambda x: x[0][0])

    next_carts = []
    while len(carts):
        cart = carts.pop(0)
        #try:
        new_cart = get_next(cart, maze[cart[0][0]][cart[0][1]])
        if new_cart[1][0] == 1 and new_cart[1][1] == 1:
            print cart, maze[cart[0][0]][cart[0][1]], new_cart
            sys.exit()
        #except:
        #    print cart
        #    print tick, carts, next_carts
        #    print_maze(maze, carts+next_carts)

        if is_collision(new_cart, next_carts + carts):
            print 'BAM', new_cart[0][1], new_cart[0][0]
            #done = True
            next_carts = [cart for cart in next_carts if not (cart[0][0] == new_cart[0][0] and cart[0][1] == new_cart[0][1])]
            carts = [cart for cart in carts if not (cart[0][0] == new_cart[0][0] and cart[0][1] == new_cart[0][1])]
        else:
            next_carts.append(new_cart)

    carts = list(next_carts)

    #if tick < 1:
    #    print_maze(maze, carts)
    #else:
    #    sys.exit()

    if len(carts) == 1:
        print carts
        done = True

    tick += 1





