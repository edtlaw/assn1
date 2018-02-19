class Cell(object):
    g = None
    h = None
    f = None
    x_cord = None
    y_cord = None
    blocked = False
    visited = False

    def __init__(self, g, h):
        self.g = 0
        self.h = 0
        self.f = g + h

    def hnewCalc(self, gs, ggoal):
        pass

class GridWorld(Cell):

    def __init__(self, size):
        self.grid = [[None for x in range(size)] for y in range(size)]
        self.size = size
        

    def buildMaze(self):
        x = randint(0, 10)
        y = randint(0, 10)
        self.grid[x][y] = Cell()
    def find