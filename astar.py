import heapq
import sys
import math
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


#fp = open(str(var) + '.txt', 'r')
#s = fp.read()
#fp.close()
maxRows=5 #101
maxCols=5 #101
toody=[[Cell(x,y,0) for y in range(maxCols)] for x in range(maxRows)]


#while

toody[0][1].blocked=1
toody[2][1].blocked=1
toody[0][3].blocked=1
toody[1][3].blocked=1
start = toody[0][0]
goal = toody[1][4]
start.g=0
start.prevCell=None



#    fp.close()


def printToody(toody,closedList):
    for x in range(maxRows):
        for y in range(maxCols):
            temp=' '
            if toody[x][y].blocked==1:
                poo('B'+temp)
            elif toody[x][y].blocked==0:
                if toody[x][y] in closedList:
                    poo('P'+temp)
                else:
                    poo('O'+temp)
        poo("\n")



#def printToody1(toody,closedList,currCell):
#    for x in range(maxRows):
            #if toody[x][y].blocked==1:
    #            poo('B'+temp)
    #            if toody[x][y] in
    #            if toody[x][y] in closedList:
    #            else:
    #                poo('O'+temp)
    #    poo("\n")









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
        printToody(toody,closedList)
        print('getting')
        curCell=heapq.heappop(openList)[1]
        closedList.append(curCell)
        if curCell is None:
            return 'failure'
        poo('curCell: '+str(curCell.x)+', '+str(curCell.y)+'\n')
        if curCell == goal:
            print('found')
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

    return 'not found'
search(start,goal)

#search
#check in order of up right left down for each action.
#calculate cost by f=g+h, where g is the actual cost accumulated up to this point, h is absolute x,y of point - goal.

#sort by priority queue for now, implement binary heap later when finished
#take lowest cost, repeat
