from GridWorld import *
from BinaryHeap import *
import pickle

def main():
    gw = GridWorld(5)
    gw.buildMaze()
    for i in range(len(gw.grid)):
        for j in range(len(gw.grid[i])):
            print(gw.grid[i][j].blocked, " ", end ="")
        print('\n')
    print('\n')
    with open('graph_1.pkl', 'wb') as output:
        pickle.dump(gw, output, pickle.HIGHEST_PROTOCOL)
    del gw
    with open('graph_1.pkl', 'rb') as input:
        gw = pickle.load(input)
        for i in range(len(gw.grid)):
            for j in range(len(gw.grid[i])):
                print(gw.grid[i][j].blocked, " ", end ="")
            print('\n')
if __name__ == '__main__':
    main()
