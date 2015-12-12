#!/usr/bin/env python
import itertools

f = open('input', 'r')

routes = dict()
cities = set()
for line in f.readlines():
    city1 = line.split(' ')[0]
    city2 = line.split(' ')[2]
    dist  = int(line.split(' ')[4])
    routes[(city1, city2)] = dist
    routes[(city2, city1)] = dist

    cities.add(city1)
    cities.add(city2)

f.close()

min_dist = max(routes.values()) * len(routes)
max_dist = 0

min_route = None
max_route = None
for route in itertools.permutations(cities):
    dist = 0
    for idx in xrange(len(route) - 1):
        dist += routes[(route[idx], route[idx+1])]

    if dist < min_dist:
        min_route = route
        min_dist = dist

    if dist > max_dist:
        max_route = route
        max_dist = dist

print 'Shortest route distance: %d' % min_dist
print 'Longest route distance: %d' % max_dist
