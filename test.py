class Cell:

    def __init__(self):
        self.visited = False
        self.f = 0
        self.g = 0
        self.h = 0
    def setVisited(self):
        self.visited = True

    def setHeur(self, g, f, h):
        self.g = g
        self.h = h
        self.f = f

