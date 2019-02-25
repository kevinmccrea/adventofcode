#!/usr/bin/env python

import sys
import collections
import itertools
import numpy

import aoc

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = [line.strip() for line in data]

def chip_image(image, block_rows, block_cols):
    """
    Take a 2D image and reshape into chips of size block_rows by block_cols.
    The returned structure is a view of the input (not a copy)
    """
    img_rows, img_cols = numpy.array(image).shape
    row_segs = img_rows / block_rows
    col_segs = img_cols / block_cols

    #return image.reshape((row_segs, col_segs, block_rows, block_cols)).transpose(0,2,1,3)
    return image.reshape((row_segs, block_rows, col_segs, block_cols)).swapaxes(1,2)

#def combine_image(image, image_rows, image_cols):
def combine_image(image):
    """
    Reshape a 4D array of image chips into a 2D array of size image_rows by
    image_cols.
    """
    row_chips, col_chips, rows, cols = image.shape
    #return image.transpose(0,2,1,3).reshape((image_rows, image_cols))
    #return image.transpose(0,2,1,3).reshape((row_chips * rows, col_chips * cols))
    return image.swapaxes(1,2).reshape((row_chips * rows, col_chips * cols))

def str2array(rule):
    return numpy.array([list(row) for row in rule.split('/')])


transforms = {}
for line in data:
    rule, transform = aoc.tokenize(line, '=>')

    rule = str2array(rule)
    transform = str2array(transform)

    transforms[str(rule)] = transform
    transforms[str(numpy.flipud(rule))] = transform
    transforms[str(numpy.fliplr(rule))] = transform

    transforms[str(numpy.rot90(rule))] = transform
    transforms[str(numpy.flipud(numpy.rot90(rule)))] = transform
    transforms[str(numpy.fliplr(numpy.rot90(rule)))] = transform

    transforms[str(numpy.rot90(numpy.rot90(rule)))] = transform
    transforms[str(numpy.flipud(numpy.rot90(numpy.rot90(rule))))] = transform
    transforms[str(numpy.fliplr(numpy.rot90(numpy.rot90(rule))))] = transform

image = str2array('.#./..#/###')

iters = 0
while iters < 18:

    if image.shape[0] == 3:
        rows = 1
        cols = 1
        chips = image.reshape((1,1,3,3))
    else:
        if image.shape[0] % 2 == 0:
            chips = chip_image(image, 2, 2)
        else:
            chips = chip_image(image, 3, 3)

        rows, cols, _, _ = chips.shape

    new_image = []
    for rr in xrange(rows):
        row = []
        for cc in xrange(cols):
            row.append(transforms[str(chips[rr][cc])])
        new_image.append(row)
    image = combine_image(numpy.array(new_image))

    iters += 1

    if iters == 5:
        part_one = list(image.flatten()).count('#')

    print 'iter:', iters

print 'Part 1:', part_one
print 'Part 2:', list(image.flatten()).count('#')

