from BinaryHeap import Cell, BinHeap

def main():
    myList = BinHeap()
    x = Cell(1, 1)
    myList.push(x)
    myList.push(Cell(3, 2))
    myList.push(Cell(0, 1))

    for x in myList.heapList:
        print(x.f)



if __name__ == '__main__':
    main()
