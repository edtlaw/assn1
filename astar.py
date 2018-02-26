import heapq
import sys
import math
import string

#print strings - poo(str(int)), didn't test any other data types
def poo(message):
    sys.stdout.write(message)
    sys.stdout.flush()

#simple cell object - might not use until later
class Cell(object):
    x=0
    y=0
    f=math.inf
    g=math.inf
    prevCell=None
    #0 for unblocked, 1 for blocked
    blocked=0
    def __init__(self,x,y,blocked):
        self.x=x
        self.y=y
        self.blocked=blocked
    def __hash__(self):
        return hash((self.x,self.y))
    def __eq__(self, other):
        return (self.x,self.y)==(other.x,other.y)
    def __ne__(self, other):
        return not(self==other)
    def __lt__(self, other):
        return self.f<other.f


#init 2d array - used example from recitation week 3 ( A* algorithm)
#want this to work first because we have a step by step example
# S  1  0  1  0
# 0  0  0  1  T
# 0  1  0  0  0
# 0  0  0  0  0
# 0  0  0  0  0

for var in list(range(50)):              #delete # to go through all 50
    input("Press Enter to continue")         #waits for user to press enter
    fp = open(str(var) + '.txt', 'r') #var for 0
    s = fp.read()
    q=s.split()
    #q is a list of numbers, every two numbers are coordinates for where the blocks are.


    fp.close()
    maxRows=101 #101
    maxCols=101 #101
    toody=[[Cell(x,y,0) for y in range(maxCols)] for x in range(maxRows)]

    qiter = iter(q)
    for numbers in qiter:
        toody[int(numbers)][int(next(qiter))].blocked=1             ##loads blocked
    x = 0
    y = 0


    #toody[0][1].blocked=1
    #toody[2][1].blocked=1
    #toody[0][3].blocked=1
    #toody[1][3].blocked=1


    toody[5][5].blocked = 0         #we should keep the goals and starts constant, idk why I made end.txts >_>
    toody[20][20].blocked = 0
    start = toody[5][5]
    goal = toody[20][20]
    start.g=0
    start.prevCell=None
    #toody[25][25].blocked = 0

    def printToody(toody,closedList,goal):   #doesn't print the "finished" iteration of the map. looks incomplete.
        for x in range(25):          #prints too much orginally maxRows
            for y in range(25):      #prints too much holy god maxCols
                temp=' '
                if toody[x][y].blocked==1:
                    poo('B'+temp)
                elif toody[x][y].blocked==0:
                    if toody[x][y] == goal:# prints too many Gs?
                        poo('G'+temp)      #otherwise prints too many Gs
                    elif toody[x][y] in closedList:
                        poo('P'+temp)
                    else:
                        poo('O'+temp)
            poo("\n")












    openList = []
    heapq.heappush(openList,(start.f,start))
    closedList = []

    #backtrack from goal to start
    def reconstructPath(curCell):
        poo(str(curCell.x) + ', ' + str(curCell.y) + '\n')
        while curCell and curCell.prevCell is not None:
            curCell=curCell.prevCell
            poo(str(curCell.x) + ', ' + str(curCell.y) + '\n')

    def findpath(curCell):
        poo(str(curCell.x) + ', ' + str(curCell.y) + '\n')
        while curCell and curCell.prevCell is not None:
            curCell=curCell.prevCell
            poo(str(curCell.x) + ', ' + str(curCell.y) + '\n')

    def manhattanDistance(cur,goal):
        return abs(cur.x-goal.x)+abs(cur.y-goal.y)

    #grid, blooks, search
    def search(start,goal):
        print('searching')
        if not openList:
            print('empty')
        while openList:
            printToody(toody,closedList,goal)
            print('getting')
            curCell=heapq.heappop(openList)[1]
            closedList.append(curCell)
            if curCell is None:
                return 'failure'
            poo('curCell: '+str(curCell.x)+', '+str(curCell.y)+'\n')
            if curCell == goal:
                print('found')
                print(len(closedList))
                return reconstructPath(curCell)
            x=curCell.x
            y=curCell.y
            #check neighbors:
            def checkNeighbor(x,y):
                if x>maxRows-1 or y>maxCols-1 or x<0 or y<0:
                    return
                nextCell = toody[x][y]
                if nextCell in closedList or nextCell.blocked:
                    return
                #actions always cost 1 unit for this grid
                tempG=curCell.g + 1
                poo('nextCell g: ' + str(nextCell.g) + 'curCell g: ' +str(curCell.g)+'\n')
                if curCell.g+1<nextCell.g:
                    print('found better path')
                    nextCell.prevCell=curCell
                    nextCell.g=tempG
                    nextCell.f=tempG+manhattanDistance(nextCell,goal)
                    poo('nextCell: ' + str(nextCell.x) + ', ' + str(nextCell.y) + '\n')
                if (nextCell.f,nextCell) not in openList:
                    heapq.heappush(openList,(nextCell.f,nextCell))

            #up,down,left,right
            checkNeighbor(x-1, y)
            checkNeighbor(x+1,y)
            checkNeighbor(x, y - 1)
            checkNeighbor(x,y+1)
        print('not found')
        return 'not found'

    search(start,goal)

    #search
    #check in order of up right left down for each action.
    #calculate cost by f=g+h, where g is the actual cost accumulated up to this point, h is absolute x,y of point - goal.

    #sort by priority queue for now, implement binary heap later when finished
    #take lowest cost, repeat
