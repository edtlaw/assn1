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
        ComputePath(world.grid, start, goal, openlist, closedlist)
        if openlist is None:
            print("I cannot reach the target")
        else:
            updateStart()


if __name__ == '__main__':
    main()

def ComputePath(grid, start, goal, open, closed):

    while goal.g > open.peek():
        s = open.popOut()
        closed.add(s)
        for x in s.neighbors:
            





def updateStart():
    pass
