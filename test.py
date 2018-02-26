from GridWorld import *


def main():
    gw = GridWorld(100)
    gw.buildMaze()
    for i in range(100):
        for j in range(100):
            print(gw.grid[i][j].blocked, " ", end= "")
        print('\n')
if __name__ == '__main__':
    main()
