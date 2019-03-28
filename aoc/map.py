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

def create_maze(data):
    """
    Creates a maze given the text input definition of data.  The maze
    is a dict of position tuples with the value being the text character at
    that position.
    """
    maze = {}
    for rr in xrange(len(data)):
        for cc in xrange(len(data[0])):
            maze[(rr,cc)] = data[rr][cc]
    return maze

def find_players(maze, player_chars=None, background_chars=None, replace_char=None):
    """
    Returns a list of the positions in a maze that contain any character
    in the list of players.  If replace_char is specified, then the
    player positions are replaced with the character specified effectively
    removing them from the maze.
    """
    player_list = []
    for pos, char in maze.iteritems():
        if (player_chars and char in player_chars) or (background_chars and char not in background_chars):
            player_list.append((pos, char))
            if replace_char:
                maze[pos] = replace_char
    return player_list
            
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

class BaseGraph():
    def neighbors(pos):
        pass

def astar_graph(graph, start, end):
    frontier = []
    frontier.append((start, 0))
    prevs = { start: None }
    costs = { start: 0 }

    while len(frontier):
        frontier.sort(key = lambda t: t[1])

        current_pos, current_dist = frontier.pop(0)

        if current_pos == end:
            break

        for next_pos, step_cost in graph.neighbors(current_pos):
            next_cost = costs[current_pos] + step_cost
            if next_pos not in costs or next_cost < costs[next_pos]:
                costs[next_pos] = next_cost
                dist = next_cost + mandist(next_pos, end) - 1
                frontier.append((next_pos, dist))
                prevs[next_pos] = current_pos

    return (prevs, costs)

def astar_graph_route(graph, start, end):
    prevs, costs = astar_graph(graph, start, end)
    return path_route(prevs, costs, start, end)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

