from GridWorld import *
from BinaryHeap import *
import pickle
import sys

def main():
    sys.setrecursionlimit(20000)





    with open('graph_21.pkl', 'rb') as input:
        gw = pickle.load(input)
        for i in range(len(gw.grid)):
            for j in range(len(gw.grid[i])):
                print(gw.grid[i][j].blocked, " ", end="")
            print('\n')

if __name__ == '__main__':
    main()
