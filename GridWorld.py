from random import *


class Cell(object):
    g = None
    h = None
    f = None
    x_cord = None
    y_cord = None
    visited = False
    blocked = False
    parent = None
    next = None
    # infinity is portrayed as float('inf')
    search = 0
    # ac (action cost) will be 1 initially but when encountered and is blocked
    # it will remember it by changing it to infinity
    ac = 1
    neighbors = set()

    def __init__(self,x,y,blocked):
        self.x = x
        self.y = y
        self.blocked = blocked

    def setHeur(self, goal):
        if self is goal:
            self.h = 0
        # self.h = put manhattan distance using goal.xcord and goal.ycord

    def calcInfo(self, goal, start):
        pass

    def hnewCalc(self, goal):
        pass


class GridWorld(Cell):

    def __init__(self):
        self.grid = [[Cell()]*5 for _ in range(5)]

    def buildMaze(self):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        self.grid[x][y] = Cell(x, y)

    def findNeighbors(self, s):

        x = s.x_cord
        y = s.y_cord
        if x > 0:
            tmp = self.grid[x-1][y]
            s.neighbors.add(tmp)
        if x < 100:
            tmp = self.grid[x+1][y]
            s.neighbors.add(tmp)
        if y > 0:
            tmp = self.grid[x][y-1]
            s.neighbors.add(tmp)
        if y < 100:
            tmp = self.grid[x][y+1]
            s.neighbors.add(tmp)