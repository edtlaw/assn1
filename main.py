from BinaryHeap import *
from GridWorld import *


def main():

    world = GridWorld()
    counter = 0
    start = world.grid[4][2]
    goal = world.grid[4][4]
    while start != goal:
        counter = counter + 1
        start.g = 0
        start.search = counter
        goal.g = float('inf')
        goal.search = counter
        openlist = BinHeap()
        closedlist = set()
        start.setHeur(goal)
        openlist.push(start)
        ComputePath(world.grid, start, goal, openlist, closedlist, counter)
        if openlist is None:
            print("I cannot reach the target")
        else:
            start = updateStart(start, goal)


if __name__ == '__main__':
    main()


def ComputePath(grid, start, goal, open, closed, counter):
    for x in start.neighbors:
        if x.blocked is True:
            x.ac = float('inf')
    while goal.g > open.peek():
        s = open.popOut()
        closed.add(s)
        s.setHeur(goal)
        for x in s.neighbors:
            if x not in closed:
                if x.search < counter:
                    x.g = float('inf')
                    x.search = counter
                if x.g > s.g + x.ac:
                    if x.blocked is True:
                        x.ac = float('inf')
                    x.parent = s
                    open.delcell(x)
                    x.f = x.g + x.h
                    open.push(x)


def updateStart(start,goal):
    tmp = goal
    while tmp is not start:
        tmp.parent.next = tmp
        tmp = tmp.parent
    while tmp.blocked is not True:
        tmp = tmp.next
    return tmp.parent
