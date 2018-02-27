from random import *
import random

class Cell(object):
    g = float('inf')
    h = None
    f = float('inf')
    x = None
    y = None
    visited = False
    blocked = False
    parent = None
    next = None
    start = False
    goal = False
    # infinity is portrayed as float('inf')
    search = 0
    # ac (action cost) will be 1 initially but when encountered and is blocked
    # it will remember it by changing it to infinity
    ac = 1

    def __init__(self):
        self.neighbors = set()

    def setHeur(self, goal):
        if self is goal:
            self.h = 0
        else:
            self.h = abs(self.x - goal.x) + abs(self.y - goal.y)

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
                        deck = list(range(1, 100))
                        random.shuffle(deck)
                        b = deck.pop()
                        if b <= 70:
                            stack.append(x)
                        else:
                            x.blocked = True


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

    def printFunc(self):
        for i in range(self.size):
            for j in range(self.size):
                c = self.grid[i][j]
                if c.goal:
                    print("x:", c.x, "y:", c.y, "|", "G", " ", end="|")
                elif c.start:
                    print("x:", c.x, "y:", c.y, "|", "S", " ", end="|")
                else:
                    if c.blocked:
                        print("x:", c.x, "y:", c.y, "|", 1, " ", end="|")
                    else:
                        print("x:", c.x, "y:", c.y, "|", 0, " ", end="|")
            print('\n')