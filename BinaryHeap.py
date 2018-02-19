class Cell(object):
    g = None
    h = None
    f = None
    blocked = False
    visited = False

    def __init__(self, g, h):
        self.g = 0
        self.h = 0
        self.f = g + h

    def calcFVal(self):
        self.f = self.g + self.h


class BinHeap(Cell):

    def __init__(self):
        self.heapList = []

    def push(self, c):
        self.heapList.append(c)
        self.percUp()

    def popOut(self):
        if len(self.heapList) < 1:
            return None
        tmp = self.heapList[0]
        self.heapList[0] = self.heapList[len(self.heapList) - 1]
        del self.heapList[len(self.heapList) - 1]
        self.percDown()
        return tmp

    def percUp(self):
        i = len(self.heapList) - 1
        while i > 0:
            p = (i-1)//2
            parent = self.heapList[p]
            item = self.heapList[i]
            if item.f < parent.f:
                self.heapList[p] = item
                self.heapList[i] = parent
                i = p
            else:
                break

    def percDown(self):
        i = 0
        while (i * 2) < len(self.heapList):
            parent = self.heapList[i]
            if self.minChildInd(i) is not None:
                c = self.heapList[self.minChildInd(i)]
                if parent.f > c.f:
                    self.heapList[i] = c
                    self.heapList[self.minChildInd(i)] = parent
                i = self.minChildInd(i)
            else:
                break

    def minChildInd(self, ind):
        mc = None
        left = 2 * ind + 1
        right = left + 1
        if left < len(self.heapList):
            mc = left
        if right < len(self.heapList):
            if self.heapList[left].f > self.heapList[right].f:
                mc = right
        return mc
