from random import *


class Cell(object):
    g = None
    h = None
    f = None
    x = None
    y = None
    visited = False
    blocked = 0
    parent = None
    next = None
    # infinity is portrayed as float('inf')
    search = 0
    # ac (action cost) will be 1 initially but when encountered and is blocked
    # it will remember it by changing it to infinity
    ac = 1
    neighbors = set()

    def __init__(self):
        pass

    def setHeur(self, goal):
        if self is goal:
            self.h = 0
        # self.h = put manhattan distance using goal.xcord and goal.ycord

    def calcInfo(self, goal, start):
        pass

    def hnewCalc(self, goal):
        pass


class GridWorld(Cell):
    unvisited_set = set()

    def __init__(self, size):
        self.size = size

        self.grid = [[Cell() for j in range(size)] for i in range(size)]

    def setCoords(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):

                self.grid[i][j].x = i
                self.grid[i][j].y = j

                self.unvisited_set.add(self.grid[i][j])
                self.findNeighbors(self.grid[i][j])

    def buildMaze(self):
        self.setCoords()
        stack = list()

        while len(self.unvisited_set) > 0:
            tmp = choice(tuple(self.unvisited_set))
            self.setVisited(tmp)
            stack.append(tmp)
            while len(stack) > 0:
                tmp = stack.pop()
                
                for x in tmp.neighbors:
                    if x.visited is False:
                        self.setVisited(x)

                        b = randint(1, 100)
                        if b <= 70:
                            stack.append(x)
                        else:
                            x.blocked = 1

        pass

    def setVisited(self, cell):
        cell.visited = True
        self.unvisited_set.remove(cell)

    def findNeighbors(self, s):

        x = s.x
        y = s.y
        if x > 0:
            tmp = self.grid[x-1][y]
            s.neighbors.add(tmp)
        if x < self.size-1:
            tmp = self.grid[x+1][y]
            s.neighbors.add(tmp)
        if y > 0:
            tmp = self.grid[x][y-1]
            s.neighbors.add(tmp)
        if y < self.size-1:
            tmp = self.grid[x][y+1]
            s.neighbors.add(tmp)