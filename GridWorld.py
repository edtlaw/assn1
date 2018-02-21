from random import *

class Cell(object):
    g = None
    h = None
    f = None
    x_cord = None
    y_cord = None
    visited = False
    parent = None
    # left, right, up, down = None
    # for action cost to portray blocked we can make it equal to infinity
    actionCost = None

    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y

    def calcInfo(self, goal, start):
        pass

    def hnewCalc(self, goal):
        pass


class GridWorld(Cell):

    def __init__(self, size):
        self.grid = [[Cell() for _ in range(size)] for _ in range(size)]
        self.size = size

    def buildMaze(self):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        self.grid[x][y] = Cell()

    def findNeighbors(self, c):
        pass