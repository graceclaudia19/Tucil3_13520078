from shutil import move
from turtle import position


def kurang(m, el, iNow, jNow):
    less = 0
    for i in range (iNow,len(m)):
        if i==iNow:
            strj = jNow
        else:
            strj = 0
        for j in range(strj,len(m[0])):
            if m[i][j] == 16:
                continue
            else:
                if el> m[i][j]:
                    less+=1
    return less

def cost(m):
    costs = 0
    ans = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]
    for i in range (len(m)):
        for j in range (len(m[0])):
            if m[i][j]!=ans[i][j]:
                costs+=1
    return costs
                
def blankPositionI(m):
    for i in range (len(m)):
        for j in range (len(m[0])):
            if m[i][j] == 16:
                return i

def blankPositionJ(m):
    for i in range (len(m)):
        for j in range (len(m[0])):
            if m[i][j] == 16:
                return j
                
def moveUp(m):
    found = False
    for i in range (len(m)):
        for j in range (len(m[0])):
            if m[i][j] == 16 and i!=0 and (not found):
                m[i][j], m[i-1][j] = m[i-1][j], m[i][j]
                found = True
    return cost(m)

    
    
def moveDown(m):
    found = False
    for i in range (len(m)):
        for j in range (len(m[0])):
            if m[i][j] == 16 and i!=len(m)-1 and (not found):
                m[i][j], m[i+1][j] = m[i+1][j], m[i][j]
                found = True
    return cost(m)
    

def moveRight(m):
    found = False
    for i in range (len(m)):
        for j in range (len(m[0])):
            if m[i][j] == 16 and j!=len(m)-1 and (not found):
                m[i][j], m[i][j+1] = m[i][j+1], m[i][j]
                found = True
    return cost(m)


def moveLeft(m):
    found = False
    for i in range (len(m)):
        for j in range (len(m[0])):
            if m[i][j] == 16 and j!=0 and (not found):
                m[i][j], m[i][j-1] = m[i][j-1], m[i][j]
                found = True
    return cost(m)

def displayMatrix(m):
    for i in range (len(m)):
        print("|", end=" ")
        for j in range (len(m[0])):
            if m[i][j]==16:
                print("  ", end=" ")
            elif m[i][j]>0 and m[i][j]<10:
                print("0"+str(m[i][j]), end=" ")
            else:
                print(str(m[i][j]), end=" ")
        print("|")   

def copyMatrix(m):
    newM = []
    for i in range(len(m)):
        newM.append([])
        for j in range(len(m[i])):
            newM[i].append(m[i][j])
    return newM

def isSame(m1, m2):
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            if m1[i][j] != m2[i][j]:
                return False
    return True

def IsNotInMatrixBefore(m, matrixesBefore):
    for matrix in matrixesBefore:
        if isSame(m, matrix):
            return False 
    return True



def solve(m, matrixesBefore):
    dirs = ["up", "right","down","left"]
    iM = blankPositionI(m)
    jM = blankPositionJ(m)
    mUp = copyMatrix(m)
    mRight = copyMatrix(m)
    mDown = copyMatrix(m)
    mLeft = copyMatrix(m)
    PuzzleToSolve = []
    PuzzleCosts = []
    Move = []
    canMoveUp = False
    canMoveRight = False
    canMoveDown = False
    canMoveLeft = False
    for i in range(len(dirs)):
        if dirs[i] == "up" and iM-1>=0:
            costUp = moveUp(mUp)
            if IsNotInMatrixBefore(mUp, matrixesBefore):
                PuzzleCosts.append(costUp)
                canMoveUp = True
        if dirs[i] == "right" and jM+1<len(m[0]):
            costRight = moveRight(mRight)
            if IsNotInMatrixBefore(mRight, matrixesBefore):
                PuzzleCosts.append(costRight)
                canMoveRight = True
        if dirs[i] == "down" and iM+1<len(m):
            costDown = moveDown(mDown)
            if IsNotInMatrixBefore(mDown, matrixesBefore):
                PuzzleCosts.append(costDown)
                canMoveDown = True
        if dirs[i] == "left" and jM-1>=0:
            costLeft = moveLeft(mLeft)
            if IsNotInMatrixBefore(mLeft, matrixesBefore):
                PuzzleCosts.append(costLeft)
                canMoveLeft = True

    PuzzleCosts.sort()

    up = False
    right = False
    down = False
    left = False
    for cost in PuzzleCosts:
        if canMoveUp and cost == costUp and not up:
            PuzzleToSolve.append(mUp)
            up = True
            Move.append("up")
        elif canMoveRight and cost == costRight and not right:
            PuzzleToSolve.append(mRight)
            right = True
            Move.append("right")
        elif canMoveDown and cost == costDown and not down:
            PuzzleToSolve.append(mDown)
            down = True
            Move.append("down")
        elif canMoveLeft and cost == costLeft and not left:
            PuzzleToSolve.append(mLeft)
            left = True
            Move.append("left")
    return PuzzleToSolve, PuzzleCosts, Move

def BnB(m, depth, numNodes, matrixesBefore):
    tempM = copyMatrix(m)
    PuzzleToSolve, PuzzleCosts, Move = solve(tempM, matrixesBefore)
    position = ["up", "right","down","left"]
    for pos in position:
        if Move[0] != pos:
            numNodes +=1
        else:
            break
    print("Move: "+str(Move[0])+"\nCost: "+str(PuzzleCosts[0])+"\nTotal nodes: "+str(numNodes))
    print("Depth: "+str(depth))
    displayMatrix(PuzzleToSolve[0])
    print()

    if PuzzleCosts[0] == 0:
        print("-- PUZZLE SOLVED! --")
    else:
        matrixesBefore.append(m)
        BnB(PuzzleToSolve[0], depth+1, numNodes, matrixesBefore)

# def firstBnB(m):
#     mBefore =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#     numNodes = 1
#     depth = 1
#     mUp = copyMatrix(m)
#     mRight = copyMatrix(m)
#     mDown = copyMatrix(m)
#     mLeft = copyMatrix(m)

#     puzzle = []
#     moveUp(mUp)
#     moveRight(mRight)
#     moveDown(mDown)
#     moveLeft(mLeft)

#     puzzle.append(mUp)
#     puzzle.append(mRight)
#     puzzle.append(mDown)
#     puzzle.append(mLeft)

#     PuzzleToSolve, PuzzleCosts, Move = solve(mBefore,m)

#     for i in range (len(puzzle)):
#         if (isNotSame(puzzle[i], PuzzleToSolve[0])):
#             numNodes +=1   
#         else:
#             break
     
#     print("Move: "+str(Move[0])+"\nCost: "+str(PuzzleCosts[0])+"\nTotal nodes: "+str(numNodes))
#     displayMatrix(PuzzleToSolve[i])
#     print()
#     print()

#     if PuzzleCosts[0] == 0:
#         print("PUZZLE SOLVED!")
#         print()
#         print()
#         print()
#     else:
#         BnB(m, PuzzleToSolve[0], depth+1, numNodes+1)
    
# check whether it can be solved or not,input matrix, return bool
def reachableGoal(m):
    totLess = 0
    # checking x
    for i in range(len(m)):
        for j in range(len(m[i])):
            if (m[i][j]==16):
                if ((i+j)%2==0):
                    x = 0
                else:
                    x = 1
            less = kurang(m, m[i][j], i, j)
            totLess += less
            # print("KURANG("+str(m[i][j])+") =", less)
    # print("SIGMA KURANG(i) =",totLess)
    # print("X = ", x)
    # print("SIGMA KURANG(i) + X =", totLess+x)
    if (x+totLess)%2==0:
        return True
    else:
        return False

# file = input("Enter file to read: ")
file = "5.txt"
with open ('../test/'+file, 'r') as f:
    m = []
    for line in f.readlines():
        m.append( [ int (x) for x in line.split(' ') ] )
    if(not reachableGoal(m)):
        print("Tidak dapat diselesaikan!")
    else:
        print("Dapat diselesaikan!")
        print("Cost: "+ str(cost(m))+"\nTotal Nodes: 1")
        print("Depth: 0")
        print("Matrix mula-mula:")

        displayMatrix(m)
        print()
        BnB(m, 1, 1, [])

