from turtle import position

from numpy import mat
import pq


def kurang(m, el, iNow, jNow):
    less = 0
    for i in range (iNow,4):
        if i==iNow:
            strj = jNow
        else:
            strj = 0
        for j in range(strj,4):
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
    for i in range (4):
        for j in range (4):
            if m[i][j] != 16:
                if m[i][j]!=ans[i][j]:
                    costs+=1
    return costs
                
def blankPosition(m):
    for i in range (4):
        for j in range (4):
            if m[i][j] == 16:
                return [i,j]
                
def moveUp(m):
    found = False
    for i in range (4):
        for j in range (4):
            if m[i][j] == 16 and i-1>=0 and (not found):
                m[i][j], m[i-1][j] = m[i-1][j], m[i][j]
                found = True

def moveDown(m):
    found = False
    for i in range (4):
        for j in range (4):
            if m[i][j] == 16 and i+1<=3 and (not found):
                m[i][j], m[i+1][j] = m[i+1][j], m[i][j]
                found = True
    

def moveRight(m):
    found = False
    for i in range (4):
        for j in range (4):
            if m[i][j] == 16 and j+1<=3 and (not found):
                m[i][j], m[i][j+1] = m[i][j+1], m[i][j]
                found = True

def moveLeft(m):
    found = False
    for i in range (4):
        for j in range (4):
            if m[i][j] == 16 and j-1>=0 and (not found):
                m[i][j], m[i][j-1] = m[i][j-1], m[i][j]
                found = True

def displayMatrix(m):
    for i in range (4):
        print("|", end=" ")
        for j in range (4):
            if m[i][j]==16:
                print("  ", end=" ")
            elif m[i][j]>0 and m[i][j]<10:
                print("0"+str(m[i][j]), end=" ")
            else:
                print(str(m[i][j]), end=" ")
        print("|")   

def copyMatrix(m):
    newM = []
    for i in range(4):
        newM.append([])
        for j in range(4):
            newM[i].append(m[i][j])
    return newM

def isSame(m1, m2):
    for i in range(4):
        for j in range(4):
            if m1[i][j] != m2[i][j]:
                return False
    return True

def IsNotInMatrixBefore(m, matrixesBefore):
    for matrix in matrixesBefore:
        if isSame(m, matrix):
            return False 
    return True

def isNotInListOfNodes(nodeToCheck, listOfNodes):
    for node in listOfNodes:
        if isSame(node.mat, nodeToCheck.mat):
            return False
    return True

def generateChildNode(parent, visitedNodes):
    generatedNodes = []

    parMatrix = copyMatrix(parent.mat)    

    # DOWN
    mDown = copyMatrix(parMatrix)
    moveDown(mDown)
    nodeDown = pq.node(parMatrix,mDown, blankPosition(mDown), cost(mDown), parent.level+1, "down")
    if isNotInListOfNodes(nodeDown, visitedNodes):
        generatedNodes.append(nodeDown)
    
    # UP
    mUp = copyMatrix(parMatrix)
    moveUp(mUp)
    nodeUp = pq.node(parMatrix,mUp, blankPosition(mUp), cost(mUp), parent.level +1, "up")
    if isNotInListOfNodes(nodeUp, visitedNodes):
        generatedNodes.append(nodeUp)
    
    # RIGHT
    mRight = copyMatrix(parMatrix)
    moveRight(mRight)
    nodeRight = pq.node(parMatrix,mRight, blankPosition(mRight), cost(mRight), parent.level+1, "right")
    if isNotInListOfNodes(nodeRight, visitedNodes):
        generatedNodes.append(nodeRight)
    
    # LEFT
    mLeft = copyMatrix(parMatrix)
    moveLeft(mLeft)
    nodeLeft = pq.node(parMatrix,mLeft, blankPosition(mLeft), cost(mLeft), parent.level+1, "left")
    if isNotInListOfNodes(nodeLeft, visitedNodes):
        generatedNodes.append(nodeLeft)

    return generatedNodes

def displayInfo(step, node):
    print("----STEP",step,"----")
    print("Cost:", node.cost)
    print("Level:", node.level)
    print("Move:", node.move)
    print("Matrix:")
    displayMatrix(node.mat)
    if node.cost!=0:
        print("\n")
    
def BnB(m):
    PQ = pq.priorityQueue()

    empty_tile_pos = blankPosition(m)
    level = 0

    parent = pq.node(None,m,empty_tile_pos, cost(m), level, "initial state")
    visitedNodes = [parent] # jawaban jawaban path -> kalo udh divisit gaboleh divisit lg
    PQ.push(parent)

    step = 0
    while not(PQ.isEmpty()):
        # pop infront of prioqueue
        parent = PQ.pop()        
        # visit parent
        visitedNodes.append(parent)

        displayInfo(step, parent)

        # check if current node is goal
        if parent.cost == 0:
            print("-- Solution Found --")
            break
        else:
            # generate child node
            childNodes = generateChildNode(parent, visitedNodes)
            # push child node to prioqueue
            for child in childNodes:
                PQ.push(child)
        step += 1



# check whether it can be solved or not,input matrix, return bool
def reachableGoal(m):
    totLess = 0
    # checking x
    for i in range(4):
        for j in range(4):
            if (m[i][j]==16):
                if ((i+j)%2==0):
                    x = 0
                else:
                    x = 1
            less = kurang(m, m[i][j], i, j)
            totLess += less
            print("KURANG("+str(m[i][j])+") =", less)
    # print("SIGMA KURANG(i) =",totLess)
    # print("X = ", x)
    print("SIGMA KURANG(i) + X =", totLess+x)
    if (x+totLess)%2==0:
        return True
    else:
        return False
