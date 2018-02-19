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

        self.percUp(len(self.heapList) - 1)

    def popout(self):
        if len(self.heapList) == 1:
            return self.heapList.pop(0)
        tmp = self.heapList[0]
        self.heapList[0] = self.heapList[len(self.heapList) - 1]
        del self.heapList[len(self.heapList) - 1]
        self.percDown()
        return tmp

    def percUp(self, i):

        while i // 2 > 0:
            if self.heapList[i // 2].f > self.heapList[i].f:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def percDown(self):
        i = 0
        while (i * 2) < len(self.heapList):

            if self.minChild(i) is not None:
                if self.heapList[i].f > self.heapList[self.minChild(i)].f:
                    tmp = self.heapList[i]
                    self.heapList[i] = self.heapList[self.minChild(i)]
                    self.heapList[self.minChild(i)] = tmp
                i = self.minChild(i)

    def minChild(self, ind):
        mc = None
        left = 2 * ind + 1
        right = left + 1
        if left < len(self.heapList):
            mc = left
        if right < len(self.heapList):
            if self.heapList[left].f > self.heapList[right].f:
                mc = right
        return mc
