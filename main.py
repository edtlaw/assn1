from BinaryHeap import Cell, BinHeap

def main():
    myList = BinHeap()
    x = Cell(1, 1)
    myList.push(x)
    myList.push(Cell(3, 2))
    # y = Cell(2, 3)
    # z = Cell(0, 1)
    # myList.push(x)
    # myList.push(y)
    # myList.push(z)
    print(myList.heapList[1].f)


if __name__ == '__main__':
    main()
