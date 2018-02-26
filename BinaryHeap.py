from GridWorld import Cell


class BinHeap(Cell):

    def __init__(self):
        self.heapList = []

    def peek(self):
        if self.heapList[0] is None:
            return None
        return self.heapList[0].f

    def push(self, c):
        self.heapList.append(c)
        self.percUp(len(self.heapList) - 1)
        return

    def popOut(self):
        if len(self.heapList) < 1:
            return None
        tmp = self.heapList[0]
        self.heapList[0] = self.heapList[len(self.heapList) - 1]
        del self.heapList[len(self.heapList) - 1]
        self.percDown(0)
        return tmp

    def percUp(self, i):
        while i > 0:
            p = (i-1)//2
            parent = self.heapList[p]
            item = self.heapList[i]
            if item.f < parent.f:
                self.heapList[p] = item
                self.heapList[i] = parent
                i = p
            elif item.f == parent.f:
                if item.g > parent.g:
                    self.heapList[p] = item
                    self.heapList[i] = parent
                    i = p
            else:
                break
        return

    def percDown(self, i):
        while (i * 2) < len(self.heapList):
            print("test:", i)
            parent = self.heapList[i]
            if self.minChildInd(i) is not None:
                minC = self.minChildInd(i)
                c = self.heapList[minC]
                if parent.f > c.f:
                    self.heapList[i] = c
                    self.heapList[minC] = parent
                    i = minC
            else:
                break
        return

    def minChildInd(self, ind):
        mc = None
        left = 2 * ind + 1
        right = left + 1
        if left < len(self.heapList):
            mc = left
        if right < len(self.heapList):
            if self.heapList[left].f > self.heapList[right].f:
                mc = right
            elif self.heapList[left].f == self.heapList[right].f:
                if self.heapList[left].g < self.heapList[right].g:
                    mc = right
        return mc

    # we need this function to delete a specific cell and update its F value
    def delcell(self, c):
        if c in self.heapList:
            last = len(self.heapList) - 1
            ind = self.heapList.index(c)
            print("index", ind)
            self.heapList[ind] = self.heapList[last]
            del self.heapList[last]
            if len(self.heapList) == 0:
                return
            if self.heapList[(ind - 1) // 2].f > self.heapList[ind].f:
                self.percUp(ind)
            else:
                self.percDown(ind)
        return
