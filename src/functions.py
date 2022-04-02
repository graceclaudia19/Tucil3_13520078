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
    print("╔════╤════╤════╤════╗")
    for i in range(4):
        print("║", end=" ")
        for j in range(4):
            el = m[i][j] 
            line = "0"+ str(el) if el < 10 else str(el)
            if el == 16: 
                line = "  "
            line = line + " │" if j != 3 else line + " ║"
            print(line, end=" ")
        if i != 3:
            print("\n╟────┼────┼────┼────╢")
    print("\n╚════╧════╧════╧════╝")    

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
    nodeDown = pq.node(parMatrix,mDown, cost(mDown), parent.level+1, "down")
    if isNotInListOfNodes(nodeDown, visitedNodes):
        generatedNodes.append(nodeDown)
    
    # UP
    mUp = copyMatrix(parMatrix)
    moveUp(mUp)
    nodeUp = pq.node(parMatrix,mUp, cost(mUp), parent.level +1, "up")
    if isNotInListOfNodes(nodeUp, visitedNodes):
        generatedNodes.append(nodeUp)
    
    # RIGHT
    mRight = copyMatrix(parMatrix)
    moveRight(mRight)
    nodeRight = pq.node(parMatrix,mRight, cost(mRight), parent.level+1, "right")
    if isNotInListOfNodes(nodeRight, visitedNodes):
        generatedNodes.append(nodeRight)
    
    # LEFT
    mLeft = copyMatrix(parMatrix)
    moveLeft(mLeft)
    nodeLeft = pq.node(parMatrix,mLeft, cost(mLeft), parent.level+1, "left")
    if isNotInListOfNodes(nodeLeft, visitedNodes):
        generatedNodes.append(nodeLeft)

    return generatedNodes

def displayInfo(step, node):
    print("-- S T E P ",step,"--")
    print("Cost  :", node.cost)
    print("Level :", node.level)
    print("Move  :", node.move)
    displayMatrix(node.mat)
    if node.cost!=0:
        print("\n")
    
def BnB(m):
    PQ = pq.priorityQueue()

    parent = pq.node(None,m,cost(m), 0, "initial state")
    visitedNodes = [parent]
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
            print("\n\( ﾟヮﾟ)/ -- YOUR PUZZLE IS SOLVED! -- ٩(◍╹∀╹◍)۶")
            break
        else:
            # generate child node
            childNodes = generateChildNode(parent, visitedNodes)
            # push child node to prioqueue
            for child in childNodes:
                PQ.push(child)
        step += 1

def displayKurangTable(kurangTable,x, totless):
    print(" -------------------")
    print("|  i   |  Kurang(i) |")
    print(" -------------------")
    for i in range(1,len(kurangTable)):
        if i<10:
            if kurangTable[i] < 10:
                print("|  0"+str(i)+"  |    ", kurangTable[i], "     |")
            else:
                print("|  0"+str(i)+"  |    ", kurangTable[i], "    |")
        else:
            if kurangTable[i] < 10:
                print("| ",i," |    ",kurangTable[i],"     |")
            else:
                print("| ",i," |    ",kurangTable[i],"    |")
    print(" -------------------")
    print("| ΣKurang(i)",str(totless),"    |")
    print("| Nilai x = ",str(x) ,"     |")
    print("| ΣKurang(i)+x =", str(totless + x), "|")
    print(" -------------------")
        


# check whether it can be solved or not,input matrix, return bool
def reachableGoal(m):
    print("""
 ██╗███████╗    ██████╗ ██╗   ██╗███████╗███████╗██╗     ███████╗    ███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗ 
███║██╔════╝    ██╔══██╗██║   ██║╚══███╔╝╚══███╔╝██║     ██╔════╝    ██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗
╚██║███████╗    ██████╔╝██║   ██║  ███╔╝   ███╔╝ ██║     █████╗      ███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝
 ██║╚════██║    ██╔═══╝ ██║   ██║ ███╔╝   ███╔╝  ██║     ██╔══╝      ╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗
 ██║███████║    ██║     ╚██████╔╝███████╗███████╗███████╗███████╗    ███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║
 ╚═╝╚══════╝    ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝    ╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝                                                                                                     
    """)
    totLess = 0
    # checking x
    kurangTable = [0 for i in range (17)]
    for i in range(4):
        for j in range(4):
            if (m[i][j]>16):
                return False
            if (m[i][j]==16):
                if ((i+j)%2==0):
                    x = 0
                else:
                    x = 1
            less = kurang(m, m[i][j], i, j)
            totLess += less
            kurangTable[m[i][j]-1] = less
    displayKurangTable(kurangTable, x, totLess)
    if (x+totLess)%2==0:
        return True
    else:
        return False
