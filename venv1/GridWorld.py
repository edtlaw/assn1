class Cell(object):
    g = None
    h = None
    f = None
    x_cord = None
    y_cord = None
    blocked = False
    visited = False
    neighbors = []

    def __init__(self, g, h):
        self.g = 0
        self.h = 0
        self.f = g + h

    def hnewCalc(self, gs, ggoal):
        pass

class GridWorld(Cell):
    grid = [[None for x in 10] for y in 10]

    def buildMaze(self):
        x = randint(0, 10)
        y = randint(0, 10)
        self.grid[x][y] = Cell()