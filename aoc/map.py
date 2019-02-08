#!/usr/bin/env python
import collections

def mandist(point1, point2):
    """
    Returns the manhatten distance between two tuples of points

    >>> mandist((0,0), (3, 4))
    7
    >>> mandist((1,2,3), (5, 1, 8))
    10
    """
    sum = 0
    for c1,c2 in zip(point1, point2):
        sum += abs(c1-c2)
    return sum

def tup_add(a, b):
    """
    Adds two tuples together element-wise

    >>> tup_add((0,0), (3,5))
    (3, 5)
    >>> tup_add((5,1), (-2, -8))
    (3, -7)
    >>> tup_add((0,1,2), (4,5,9))
    (4, 6, 11)
    """
    return tuple([aa + bb for aa, bb in zip(a, b)])

def astar(maze, start, end, directions, walls):
    frontier = []
    frontier.append((start, 0))
    prevs = { start: None }
    costs = { start: 0 }

    while len(frontier):
        frontier.sort(key = lambda t: t[1])

        current_pos, current_dist = frontier.pop(0)

        if current_pos == end:
            break

        for step in directions:
            next_pos = tup_add(current_pos, step)
            
            if maze[next_pos] in walls:
                continue

            next_cost = costs[current_pos] + 1
            if next_pos not in costs or next_cost < costs[next_pos]:
                costs[next_pos] = next_cost
                dist = next_cost + mandist(next_pos, end) - 1
                frontier.append((next_pos, dist))
                prevs[next_pos] = current_pos

    return (prevs, costs)

def path_route(prevs, costs, start, end):
    if not prevs.has_key(end):
        return None

    curr = end
    route = collections.deque()
    while curr != start:
        route.appendleft(curr)
        curr = prevs[curr]
    return route

def astar_route(maze, start, end, directions, walls):
    prevs, costs = astar(maze, start, end, directions, walls)
    return path_route(prevs, costs, start, end)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

