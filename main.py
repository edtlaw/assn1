from BinaryHeap import *
from GridWorld import *

def main():
    l = BinHeap()
    x = Cell(2, 3)
    x.g = 1
    x.h = 1
    x.f = 1
    y = Cell(4, 5)
    y.g = 2
    y.h = 3
    y.f = 9
    z = Cell(2, 5)
    z.f = 22
    j = Cell(3, 2)
    j.f = 10
    k = Cell(1, 4)
    k.f = 11
    o = Cell(2, 1)
    o.f = 33
    q = Cell(0, 0)
    q.f = 27
    w = Cell(5, 4)
    w.f = 18
    a = Cell(4, 4)
    a.f = 19

    l.push(x)
    l.push(y)
    l.push(z)
    l.push(j)
    l.push(k)
    l.push(o)
    l.push(q)
    l.push(w)
    l.push(a)


    l.delcell(y)
    for i in l.heapList:
        print(i.f)
if __name__ == '__main__':
    main()
